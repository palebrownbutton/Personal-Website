import React, { useRef } from 'react';
import './Projects.css';
import { useState } from 'react';

export default function SpriteController() {
    const totalFrames = 9;
    const [frame, setFrame] = useState(0);
    const frameWidth = 171;
    const frameHeight = 114;

    const animating = useRef(false);

    const playAnimation = (direction = 1) => {

        if (animating.current) return;
        animating.current = true;

        let count = 0
        const interval = setInterval(() => {
            setFrame((f) => (f + direction + totalFrames) % totalFrames);
            count++;

            if (count === totalFrames) {
                clearInterval(interval);
                animating.current = false
            }
        }, 80);
    };

    const nextFrame = () => setFrame((prevFrame) => (prevFrame + 1) % totalFrames);
    const prevFrame = () => setFrame((prevFrame) => (prevFrame - 1 + totalFrames) % totalFrames);

    const cols = 3;
    const row = Math.floor(frame / cols);
    const col = frame % cols;

    const backgroundPosition = `-${col * frameWidth}px -${row * frameHeight}px`;

    return (
        <div>
            <div className='sprite' style={{ backgroundPosition }}></div>
            <button onClick={prevFrame}>◀</button>
            <button onClick={nextFrame}>▶</button>
        </div>
    );
}