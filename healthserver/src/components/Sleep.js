import React from 'react';
import { Line } from 'react-chartjs-2';

const Sleep = ({ data, text }) => {
    return (
        <Line options={{
            responsive: true,
            aspectRatio: 1.5, // Adjust this value to change the aspect ratio
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: "",
                },
            },
            scales: {
                y: {
                    beginAtZero: false,
                    suggestedMin: text.includes('Light') ? 320 : 60,
                    suggestedMax: text.includes('Light') ? 400 : 180
                }
            }
        }} data={data} />
    );
};

export default Sleep;