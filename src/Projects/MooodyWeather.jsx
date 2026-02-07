import React, { useState } from "react";
import { FiDownload, FiGithub, FiHome } from "react-icons/fi";
import "../Projects.css"
import SpecialCowPage from "../../MooodyWeather/special";
import "../../MooodyWeather/special.css";

export default function MooodyWeather(){
    const [page, setPage] = useState("main");

    if (page === "special" ) {
        return <SpecialCowPage setPageFunction={setPage} />
    }

    return (
        <div className="game-page">
            <div className="game-inner">
                <h1 className="project-title">Mooody Weather</h1>

                <div className="demo-wrapper">
                    <div className="demo-container">
                        <SpecialCowPage />
                    </div>
                </div>
                <a
                href="https://github.com/SafiaEzzahir/cow"
                className="github-link"
                target="_blank"
                rel="noopener noreferrer"
                >
                <FiGithub style={{ marginRight: "8px" }} />
                GitHub Repository
                </a>
            </div>
            <a href="/" className="home-button">
                <FiHome />
            </a>
        </div>
    )
}