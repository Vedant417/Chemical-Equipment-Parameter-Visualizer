import React, { useState } from "react";
import Header from "../components/Header";
import "../App.css";

function Profile() {
  const [editMode, setEditMode] = useState(false);
  const [message, setMessage] = useState("");

  const [username, setUsername] = useState(
    localStorage.getItem("username") || ""
  );
  const [email, setEmail] = useState(
    localStorage.getItem("email") || ""
  );

  const [avatar, setAvatar] = useState(
    localStorage.getItem("avatar") || null
  );

  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  // Avatar upload
  const handleAvatarChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onloadend = () => {
      localStorage.setItem("avatar", reader.result);
      setAvatar(reader.result);
    };
    reader.readAsDataURL(file);
  };

  // Save changes
  const handleSave = () => {
    localStorage.setItem("username", username);
    localStorage.setItem("email", email);

    setEditMode(false);
    setMessage("Profile updated successfully ✅");

    // Clear passwords
    setCurrentPassword("");
    setNewPassword("");
    setConfirmPassword("");

    // Auto fade message (like CSV upload)
    setTimeout(() => setMessage(""), 3000);
  };

  const avatarLetter = username ? username[0].toUpperCase() : "U";

  return (
    <div className="app-container">
      <Header />

      <main className="main-content">
        <section className="glass-card profile-card">

          {/* AVATAR */}
          <div className="avatar-wrapper">
            {avatar ? (
              <img src={avatar} alt="Avatar" className="avatar-img" />
            ) : (
              <div className="avatar-circle">{avatarLetter}</div>
            )}
          </div>

          {editMode && (
            <label className="avatar-upload-btn">
              Change Avatar
              <input type="file" hidden accept="image/*" onChange={handleAvatarChange} />
            </label>
          )}

          <h2 className="profile-title">Profile</h2>

          {/* ===== VIEW MODE ===== */}
          {!editMode && (
            <div className="profile-view">
              <div className="profile-row">
                <span>Username</span>
                <strong>{username}</strong>
              </div>

              <div className="profile-row">
                <span>Email</span>
                <strong>{email}</strong>
              </div>

              <button
                className="primary-btn"
                onClick={() => setEditMode(true)}
              >
                Edit Profile
              </button>
            </div>
          )}

          {/* ===== EDIT MODE ===== */}
          {editMode && (
            <div className="profile-form">
              <div className="profile-field">
                <label>Username</label>
                <input
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
              </div>

              <div className="profile-field">
                <label>Email</label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>

              <hr className="profile-divider" />

              <h3>Change Password</h3>

              <div className="profile-field">
                <label>Current Password</label>
                <input
                  type="password"
                  value={currentPassword}
                  onChange={(e) => setCurrentPassword(e.target.value)}
                />
              </div>

              <div className="profile-field">
                <label>New Password</label>
                <input
                  type="password"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                />
              </div>

              <div className="profile-field">
                <label>Confirm New Password</label>
                <input
                  type="password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
              </div>

              <div className="profile-actions">
                <button className="primary-btn" onClick={handleSave}>
                  Save
                </button>
                <button
                  className="secondary-btn"
                  onClick={() => setEditMode(false)}
                >
                  Cancel
                </button>
              </div>
            </div>
          )}

          {/* SUCCESS MESSAGE */}
          {message && <p className="success-toast">{message}</p>}

        </section>
      </main>
    </div>
  );
}

export default Profile;
