import React from "react";
import { FiDownload } from "react-icons/fi";
import "./BonesAndBlades.css"

export default function BonesAndBlades(){
    return (
        <div className="game-page">
            <h1 className="project-title">Bones and Blades</h1>
            <a href="/bones-andblades.zip" className="download-button" download> 
                <FiDownload style={{marginRight: "8px"}} />
                Download Game
            </a>
        </div>
    )
}