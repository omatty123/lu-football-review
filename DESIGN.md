---
name: Lawrence Football Statistical Review
description: A compact, sourced statistical report with readable charts and direct access to evidence.
colors:
  ink: "#162934"
  muted: "#53616b"
  paper: "#faf9f5"
  lawrence-blue: "#08658e"
  opponent-red: "#aa372c"
  losses: "#dbada6"
  rule: "#d5d8d5"
  dark-panel: "#142b39"
  explorer: "#eef1ef"
typography:
  display:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "clamp(42px, 4.6vw, 64px)"
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: "-.02em"
  headline:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "38px"
    fontWeight: 600
    lineHeight: 1.08
  title:
    fontFamily: "Barlow Condensed, sans-serif"
    fontSize: "26px"
    fontWeight: 600
    lineHeight: 1.08
  body:
    fontFamily: "Public Sans, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
rounded:
  square: "0px"
---

# Design System: Lawrence Football Statistical Review

## Overview

The built design is a compact statistical report. Condensed headings establish hierarchy; plain body text explains the evidence. Charts, tables, dated scope notes and source links carry the page. This document records the implemented system, not a proposed redesign.

## Colors

Lawrence blue identifies scored points, wins and links. Opponent red identifies points allowed and negative margins; muted rose identifies losses in the record chart. Ink and muted text sit on warm paper. Rules divide sections. The dark panel emphasizes the 2025 analysis; a pale surface groups the game explorer. Text labels accompany chart colors.

## Typography

All type is sans-serif, including chart text and fallbacks. Locally hosted Barlow Condensed supplies headings and large figures; Public Sans supplies prose, labels and tables. Numbers use tabular forms. Captions use smaller muted text. Table headings are compact uppercase labels.

At widths up to 600px, the main heading is 44px, section headings 32px, smaller headings 25px and body text 15px. Headings wrap naturally. Never add decorative line breaks or narrow heading widths to force a dramatic arrangement.

## Layout

The page uses a centered container with a maximum width of 1280px and 48px side padding. Side padding becomes 24px below 850px. Desktop analysis sections use two or three columns; they become single columns below 600px. The masthead is compact and its navigation moves below the wordmark on mobile.

Sections use thin dividers and 44px vertical padding, reduced to 30px on mobile. Charts retain a 690px minimum width on mobile and scroll horizontally. Season and game tables also scroll within their own containers. Visible captions explain chart scrolling. The document body must not overflow horizontally.

## Elevation & Depth

The design is flat, with no shadows. Background tone, thin rules and spacing distinguish sections and controls.

## Shapes

Panels, tables and the season selector have square corners. Circular chart markers and legend dots are the recurring rounded elements. There are no decorative image frames or floating cards.

## Components

- **Scoring chart:** two labeled line series generated from the season dataset, with a zero-based scale and a visible break for canceled 2020. Exact figures remain available in the season table.
- **Record chart:** stacked wins and losses, with explicit record labels. Bar height represents completed games. Canceled and incomplete seasons are marked.
- **Season table:** aligned numerical columns, muted red recent-season rows and pale blue current-season row. Underlined year buttons select the game explorer and move focus to its selector.
- **Game explorer:** pale rectangular panel, native season selector and source-linked results table. The summary announces updates through a polite live region.
- **2025 panel:** dark background, light text, pale links and a nine-game score strip. Zero scores receive a muted red accent.
- **Evidence disclosures:** native expandable details with bold summaries and source links. Source discrepancies are initially expanded.
- **Links and controls:** underlined content links, stronger underline on hover and a visible amber focus outline. Navigation is plain text with hover underlining. Reduced-motion preference disables smooth scrolling.

## Do's and Don'ts

- Do preserve compact headers, natural wrapping and full-width evidence displays.
- Do keep chart legends, record labels, incomplete-season markers and exact table values together.
- Do keep source links readable and visually identifiable.
- Do inspect desktop and mobile output after layout or typography changes.
- Don't introduce serif type, decorative heading breaks, oversized hero areas or ornamental shadows.
- Don't communicate meaning through color alone or hide source limitations behind visual polish.

## October 18 prominence update

The opening now emphasizes the 19-game current losing streak through October 17, 2026, and links the last victory. The original 1–38 metric remains in the summary row. A dedicated VICTORY GRAPH precedes scoring analysis: sixteen columns on desktop, two rows of eight on mobile, exact win labels, canceled 2020 and incomplete 2026. The original wins/losses comparison is retained. The streak decomposition explicitly excludes the canceled Knox game.

## Super losses
The Super losses section follows the victory graph and precedes scoring analysis. A dark navy feature prominently compares Chicago’s 9 touchdowns to Lawrence’s ONE first down. The complete 15-row source-linked table highlights the Chicago row. Definitions exclude equal counts, with the two equality cases separately identified. Navigation and summary link directly to this section. Mobile retains readable numbers and scrolls the full table horizontally.

## Conference comparison and sharing
A 2025 all-ten-team comparison follows SUPER LOSSES. A centered-zero horizontal margin chart accompanies the complete table; Lawrence uses a pale red row. Three findings introduce the evidence, with all 12 peer SUPER LOSSES in an expandable table and explicit period/postseason caveats. The masthead Share button uses an outlined upload/share SVG and visible text. A visitor click opens native sharing where supported, otherwise copies the canonical URL; clipboard denial reveals a selectable link and announced status. The button never initiates sharing on page load.
