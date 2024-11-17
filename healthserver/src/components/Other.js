import React from 'react';
import { Line } from 'react-chartjs-2';

const Other = ({ data, text }) => {
    // clamp the data to a minimum of 0
    for (let i = 0; i < data.datasets[0].data.length; i++) {
        data.datasets[0].data[i] = Math.max(data.datasets[0].data[i], 0);
    }

    return (
        <Line options={
        {
            responsive: true,
            aspectRatio: 1.5, // Adjust this value to change the aspect ratio
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: text,
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 10,
                },
            }
        }} data={data} />
    );
};

export default Other;