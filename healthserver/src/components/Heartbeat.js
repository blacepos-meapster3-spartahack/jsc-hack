import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart } from 'chart.js';

const Heartbeat = ({ data, text }) => {
    return (
        <Line options={
        {
            responsive: true,
            aspectRatio: 1.5, // Adjust this value to change the aspect ratio
            plugins: {
                legend: {
                    position: 'top',
                    display: true,
                    labels: {
                        generateLabels: (chart) => {
                            const original = Chart.defaults.plugins.legend.labels.generateLabels;
                            const labels = original.call(this, chart);
                            labels.push({
                                text: 'Predicted Heart Rate',
                                fillStyle: 'rgba(255, 99, 132, 0.2)',
                                strokeStyle: 'rgba(255, 99, 132, 1)',
                                lineWidth: 1,
                                hidden: false
                            });
                            return labels;
                        }
                    }
                },
                title: {
                    display: true,
                    text: text,
                },
            },
            elements: {
                point: {
                    radius: 0
                }
            },
        }} data={data} />
    );
};

export default Heartbeat;