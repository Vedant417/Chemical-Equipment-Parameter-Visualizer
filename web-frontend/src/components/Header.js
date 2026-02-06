import React, { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Header() {
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const dropdownRef = useRef(null);

  const scrollTo = (id) => {
    document.getElementById(id)?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
    setOpen(false);
  };

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <header className="header top-header">
      <div className="logo">
        ChemEquip <span>Visualizer</span>
      </div>

    <nav className="nav-links">

      {/* HOME BUTTON */}
      <button onClick={() => navigate("/dashboard")}>
        Home
      </button>

      <button onClick={() => scrollTo("summary-anchor")}>
        Summary
      </button>

      <button onClick={() => scrollTo("charts-anchor")}>
        Charts
      </button>

      <button onClick={() => scrollTo("history-section")}>
        Upload History
      </button>


        <div className="more-wrapper" ref={dropdownRef}>
          <button
            className="more-btn"
            onClick={() => setOpen((prev) => !prev)}
          >
            More <span className="arrow">{open ? "▲" : "▼"}</span>
          </button>

          {open && (
            <div className="more-dropdown">
              <button onClick={() => navigate("/profile")}>
                👤 Profile
              </button>
              <button
                className="logout-item"
                onClick={() => navigate("/login")}
              >
                🚪 Logout
              </button>
            </div>
          )}
        </div>
      </nav>
    </header>
  );
}

export default Header;