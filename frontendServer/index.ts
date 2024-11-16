
const HTML = `<div style="width: 50%;">
    <canvas id="myChart"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
    const ctx = document.getElementById('myChart');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>`;

const server = Bun.serve({
    port: 3000,
    fetch(req) {
      return new Response(HTML, {
        headers: { "Content-Type": "text/html" },
      });
    },
  });
  
  console.log(`Listening on http://localhost:${server.port} ...`);