---
title: Faerun Kampagne Übersicht
description: Navigation zu allen Ordnern und Dokumenten der Kampagne
---

<style>
:root {
  color-scheme: light;
  color: #111827;
  background: #f8fafc;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: #f8fafc;
}

.home-container {
  max-width: 1080px;
  margin: 0 auto;
  padding: 1.5rem 1.25rem 3rem;
}

.hero {
  padding: 1.5rem 1.25rem;
  border-radius: 22px;
  background: linear-gradient(135deg, #e0f2fe 0%, #f8fafc 100%);
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
}

.hero h1 {
  margin: 0 0 0.6rem;
  font-size: clamp(2rem, 3.5vw, 3rem);
  line-height: 1.05;
}

.hero p {
  margin: 0;
  color: #475569;
  font-size: 1rem;
  line-height: 1.7;
}

.home-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  margin-top: 1.75rem;
}

.card {
  display: block;
  padding: 1.3rem;
  border-radius: 20px;
  background: #ffffff;
  border: 1px solid rgba(148, 163, 184, 0.18);
  box-shadow: 0 18px 38px rgba(15, 23, 42, 0.08);
  color: #0f172a;
  text-decoration: none;
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}

.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 26px 48px rgba(15, 23, 42, 0.12);
  border-color: rgba(59, 130, 246, 0.3);
}

.card h3 {
  margin: 0 0 0.5rem;
  font-size: 1.05rem;
}

.card p {
  margin: 0;
  color: #475569;
  font-size: 0.98rem;
  line-height: 1.6;
}

.section {
  margin-top: 2.4rem;
}

.section h2 {
  margin-bottom: 0.75rem;
  font-size: 1.5rem;
}

.link-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.link-list li {
  margin: 0.45rem 0;
}

.link-list a {
  color: #2563eb;
  text-decoration: none;
}

.link-list a:hover {
  text-decoration: underline;
}

.note {
  color: #475569;
  font-size: 0.98rem;
  margin-top: 0.75rem;
}
</style>

<div class="home-container">
  <section class="hero">
    <h1>Faerun Kampagne Übersicht</h1>
    <p>Eine zentrale Startseite für schnellen Zugriff auf alle Kampagnen-Dokumente und Ordner. Diese Seite ist als Navigation für GitHub Pages gedacht.</p>
  </section>

  <section class="section">
    <h2>Schnellzugriff</h2>
    <div class="home-grid">
      <a class="card" href="/campain-timeline.html">
        <h3>Kampagnen-Timeline</h3>
        <p>Chronologische Übersicht der Kampagne und wichtige Meilensteine.</p>
      </a>
      <a class="card" href="/house-rules.html">
        <h3>Hausregeln</h3>
        <p>Regeln und Anpassungen, die speziell für diese Kampagne gelten.</p>
      </a>
      <a class="card" href="/plot/readme.html">
        <h3>Plot</h3>
        <p>Plot-relevante Details, Hintergründe und Story-Notizen.</p>
      </a>
      <a class="card" href="/session-notes/session-0.html">
        <h3>Session-Notizen</h3>
        <p>Berichte und wichtige Informationen zur letzten Spielsitzung.</p>
      </a>
    </div>
  </section>

  <section class="section">
    <h2>Bereiche</h2>
    <div class="home-grid">
      <a class="card" href="/encounters/combat/readme.html">
        <h3>Encounters</h3>
        <p>Combat- und Social-Encounters zur Planung von Begegnungen.</p>
      </a>
      <a class="card" href="/location/citys/readme.html">
        <h3>Location</h3>
        <p>Städte, Dungeons und Regionen für Abenteuerorte.</p>
      </a>
      <a class="card" href="/loot/magical-items/readme.html">
        <h3>Loot</h3>
        <p>Magische Gegenstände und Belohnungen.</p>
      </a>
      <a class="card" href="/npcs/readme.html">
        <h3>NPCs</h3>
        <p>Wichtige NSCs und Charakterbeschreibungen.</p>
      </a>
    </div>
  </section>

  <section class="section">
    <h2>Alle Dokumente</h2>
    <ul class="link-list">
      <li><a href="/README.html">README</a> – Repository-Informationen und Überblick.</li>
      <li><a href="/campain-timeline.html">campain-timeline.md</a></li>
      <li><a href="/house-rules.html">house-rules.md</a></li>
      <li><a href="/plot/readme.html">plot/readme.md</a></li>
      <li><a href="/npcs/readme.html">npcs/readme.md</a></li>
      <li><a href="/encounters/combat/readme.html">encounters/combat/readme.md</a></li>
      <li><a href="/encounters/social/readme.html">encounters/social/readme.md</a></li>
      <li><a href="/location/citys/readme.html">location/citys/readme.md</a></li>
      <li><a href="/location/dungeons/readme.html">location/dungeons/readme.md</a></li>
      <li><a href="/location/regions/readme.html">location/regions/readme.md</a></li>
      <li><a href="/loot/magical-items/readme.html">loot/magical-items/readme.md</a></li>
      <li><a href="/session-notes/session-0.html">session-notes/session-0.md</a></li>
    </ul>
    <p class="note">Wenn eine Seite nicht sofort angezeigt wird, kann es sein, dass GitHub Pages die Markdown-Datei noch nicht in HTML umgewandelt hat. In diesem Fall hilft ein Commit oder ein erneuter Push.</p>
  </section>
</div>
