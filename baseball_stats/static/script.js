let players = [];
let teams = new Set();
let positions = new Set();

async function fetchPlayers() {
    const response = await fetch('http://localhost:5000/api/players');
    players = await response.json();
    
    // Extract unique teams and positions
    players.forEach(player => {
        teams.add(player.team);
        positions.add(player.position);
    });

    // Populate filter dropdowns
    const teamFilter = document.getElementById('team-filter');
    Array.from(teams).sort().forEach(team => {
        const option = document.createElement('option');
        option.value = team;
        option.textContent = team;
        teamFilter.appendChild(option);
    });

    const positionFilter = document.getElementById('position-filter');
    Array.from(positions).sort().forEach(position => {
        const option = document.createElement('option');
        option.value = position;
        option.textContent = position;
        positionFilter.appendChild(option);
    });

    displayPlayers();
}

function displayPlayers() {
    const tbody = document.getElementById('players-body');
    const teamFilter = document.getElementById('team-filter').value;
    const positionFilter = document.getElementById('position-filter').value;
    const sortBy = document.getElementById('sort-by').value;

    // Filter players
    let filteredPlayers = players.filter(player => {
        const teamMatch = !teamFilter || player.team === teamFilter;
        const positionMatch = !positionFilter || player.position === positionFilter;
        return teamMatch && positionMatch;
    });

    // Sort players
    if (sortBy) {
        filteredPlayers.sort((a, b) => {
            if (a[sortBy] === null) return 1;
            if (b[sortBy] === null) return -1;
            return b[sortBy] - a[sortBy];
        });
    }

    // Display players
    tbody.innerHTML = '';
    filteredPlayers.forEach(player => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${player.name}</td>
            <td>${player.team}</td>
            <td>${player.position}</td>
            <td>${player.batting_average?.toFixed(3) || '-'}</td>
            <td>${player.home_runs || '-'}</td>
            <td>${player.rbi || '-'}</td>
            <td>${player.ops?.toFixed(3) || '-'}</td>
            <td>${player.era?.toFixed(2) || '-'}</td>
            <td>${player.wins || '-'}</td>
            <td>${player.losses || '-'}</td>
            <td>${player.saves || '-'}</td>
            <td>${player.strikeouts || '-'}</td>
        `;
        tbody.appendChild(row);
    });
}

// Add event listeners
document.getElementById('team-filter').addEventListener('change', displayPlayers);
document.getElementById('position-filter').addEventListener('change', displayPlayers);
document.getElementById('sort-by').addEventListener('change', displayPlayers);

// Initial load
fetchPlayers();
