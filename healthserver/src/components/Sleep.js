import React from 'react';
import { Line } from 'react-chartjs-2';

const Sleep = ({ data, text }) => {
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
        }} data={data} />
    );
};

export default Sleep;