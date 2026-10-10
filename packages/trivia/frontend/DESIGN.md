---
name: Academic Salon Trivia
colors:
  surface: '#f6fbef'
  surface-dim: '#d7dcd1'
  surface-bright: '#f6fbef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f5ea'
  surface-container: '#ebf0e4'
  surface-container-high: '#e5eade'
  surface-container-highest: '#dfe4d9'
  on-surface: '#181d16'
  on-surface-variant: '#42493c'
  inverse-surface: '#2d322a'
  inverse-on-surface: '#eef2e7'
  outline: '#73796b'
  outline-variant: '#c2c9b8'
  surface-tint: '#3d6921'
  primary: '#37641b'
  on-primary: '#ffffff'
  primary-container: '#4f7d32'
  on-primary-container: '#e6ffd1'
  inverse-primary: '#a1d57f'
  secondary: '#785a00'
  on-secondary: '#ffffff'
  secondary-container: '#ffd16b'
  on-secondary-container: '#775800'
  tertiary: '#765300'
  on-tertiary: '#ffffff'
  tertiary-container: '#956a00'
  on-tertiary-container: '#fff6ee'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bdf298'
  primary-fixed-dim: '#a1d57f'
  on-primary-fixed: '#092100'
  on-primary-fixed-variant: '#255108'
  secondary-fixed: '#ffdf9d'
  secondary-fixed-dim: '#edc05b'
  on-secondary-fixed: '#251a00'
  on-secondary-fixed-variant: '#5b4300'
  tertiary-fixed: '#ffdea8'
  tertiary-fixed-dim: '#fcbb35'
  on-tertiary-fixed: '#271900'
  on-tertiary-fixed-variant: '#5e4200'
  background: '#f6fbef'
  on-background: '#181d16'
  surface-variant: '#dfe4d9'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 44px
    fontWeight: '700'
    lineHeight: 52px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 34px
    fontWeight: '700'
    lineHeight: 42px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.04em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.06em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-lg: 2rem
  margin: 2.5rem
  margin-wide: 4rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
  space-2xl: 4rem
---

## Brand & Style

This design system draws its spirit from the intersection of a mid-century academic salon, high-stakes parlor games, and a vibrant contemporary quiz broadcast. It balances intellectual gravitas with theatrical wit.

### Aesthetic Foundation
- **Tactile Editorial Meets Retro Broadcast**: Tactile card stock surfaces, crisp inset rules, and solid mechanical drops shadow elements recall vintage encyclopedias and mid-century game show podiums without tipping into kitsch.
- **Tone of Voice & Mood**: Erudite, celebratory, energetic, and articulate. The visual rhythm invites curiosity, rewards deep knowledge, and elevates the act of trivia into a distinguished cultural sporting event.
- **Target Audience**: Culture enthusiasts, trivia aficionados, casual scholars, and social competitors seeking a desktop quiz environment that feels substantively curated rather than gamified with juvenile candy-coated tropes.

## Colors

The palette balances warm organic neutrals against high-saturation game accents to deliver an intellectual parlor environment.

### Color Mapping
- **Primary Olive (`#4F7D32`)**: Used for authoritative actions, category badges, confirmed correct states, master scoreboards, and structural anchor blocks.
- **Golden Maize (`#FFD16A`)**: Used for spotlight cards, highlighted query prompts, active selection borders, and podium markers.
- **Marigold Amber (`#F5B52E`)**: Reserved for time-critical counters, milestone streaks, score multipliers, and energetic focal points.
- **Crimson Alert (`#D9361E`)**: Applied to strikes, critical final 5-second countdown triggers, incorrect answers, and high-stakes wagers.
- **Canvas & Surface Neutrals**:
  - Base Canvas: Cream (`#FBF9F3`) providing warm, low-glare paper ambiance.
  - Surface Containers: Calendered Paper (`#F4EFE6`) for cards, answer trays, and popover panels.
  - Ink Body: Deep Forest Ink (`#1E231C`) for high-legibility body, display copy, and crisp structural borders.

## Typography

Typography establishes tension between literary authority and modern game-engine clarity.

- **Headline Hierarchy (`Playfair Display`)**: Features high-contrast serifs, sharp terminals, and sculpted ink traps that evoke vintage quiz placards and editorial journals. Used for large trivia prompts, category titles, and dramatic round summaries.
- **Interface & Content (`Plus Jakarta Sans`)**: Delivers geometric, humanist clarity to answer options, statistical leaderboards, and meta tags. Its wide counters maintain instant legibility under timed duress.
- **Stylistic Conventions**: Trivia prompts use sentence case with typographic quotation marks. Category and metadata labels use uppercase tracking (`+0.04em` to `+0.08em`) to mimic stamped card stock classifications.

## Layout & Spacing

The layout is built for desktop-first play, establishing balanced focus without cognitive overload.

### Grid & Composition
- **12-Column Structured Centerpiece**: Uses a desktop grid constrained to a `1280px` maximum content width, centered with `4rem` outer safety margins (`margin-wide`).
- **Trivia Core Canvas**: During active rounds, the UI shifts into an 8-column central theatrical arena flanked by two 2-column rails (Player Scoreboard & Category History / Streaks).
- **Component Padding Scale**: Internal answer options adhere strictly to `space-md` vertical padding and `space-lg` horizontal padding to maintain substantial touch targets and confident cursor interaction.

## Elevation & Depth

Depth is established through physical, tactile print mechanics rather than digital blurs.

### Elevation Levels
- **Level 0 (Parchment Base)**: `#FBF9F3` flat field with an optional fine 1px structural grid delimiter (`rgba(30, 35, 28, 0.08)`).
- **Level 1 (Cardstock Surface)**: `#F4EFE6` with a crisp `2px solid #1E231C` perimeter border and an intentional, hard offset shadow: `3px 3px 0px #1E231C`.
- **Level 2 (Active Interactive Element / Answer Tile)**: Elevated answer cards use `2px solid #1E231C` with `4px 4px 0px #1E231C`. Hover states translate `-2px, -2px` and expand the offset to `6px 6px 0px #1E231C`.
- **Level 3 (Modal / Countdown Overlay)**: Floating game drawers and milestone reveals employ `8px 8px 0px #1E231C` alongside a `rgba(30, 35, 28, 0.45)` backdrop wash to retain focused theater lighting.

## Shapes

The geometry balances structured mid-century cards with friendly, modern rounded elements.

- **Primary Geometry (`0.5rem` / `8px`)**: Standard buttons, question containers, and status cards utilize balanced curvature to keep card decks feeling crisp yet approachable.
- **Large Assemblies (`1rem` / `16px`)**: Master question display boards and round recap modals leverage `rounded-lg` contours.
- **Embossed Category Badges & Pills (`9999px`)**: Category tags, countdown clocks, and status counters employ pill-shaped outlines paired with thick borders to evoke physical tokens and archival stamps.

## Components

### Buttons & Answer Tiles
- **Answer Selection Buttons**: Arranged in a 2x2 grid or vertical card stack. Encased in a `2px solid #1E231C` border with `#F4EFE6` background. Left-aligned label contains an index pill (`A`, `B`, `C`, `D`) set in Olive `#4F7D32` with white text.
- **Hover State**: Shifts upwards by 2px with an accent border glow of Golden Maize (`#FFD16A`) and a crisp `4px 4px 0px #1E231C` shadow.
- **Correct State**: Shifts to Deep Olive Forest Green (`#4F7D32`) background, crisp white text, and a checkmark insignia.
- **Incorrect / Strike State**: Flashes Crimson Red (`#D9361E`), shaking horizontally with strike icons.

### Category Chips
- Pill contours featuring individual cultural signatures:
  - *History*: Amber ground with dark ink border.
  - *Art & Architecture*: Maize ground with olive border.
  - *Cinema & Pop Culture*: Cream ground with crimson border.
  - *Literature & Philosophy*: Deep Olive ground with gold text.
- Always accompanied by uppercase `label-sm` typography and a geometric micro-icon.

### Countdown Timer
- Circular or bar format utilizing a solid-stroke perimeter.
- Base ring: `4px solid #1E231C`.
- Active fill: Transitions from `#4F7D32` (Normal), to `#F5B52E` (10 seconds remaining), to a pulsating `#D9361E` (Final 5 seconds) accompanied by crisp monospace-inspired countdown numbers.

### Trivia Question Card
- Centered stage element framed by a dual inset border (a `2px solid #1E231C` outer border and an inner `1px dashed rgba(30, 35, 28, 0.25)` hairline).
- Prominently showcases the question prompt in `headline-lg` (`Playfair Display`) with generous line spacing for effortless reading across the desk.

### Score Milestones & Streaks
- Embossed wooden-and-brass aesthetics rendered cleanly: `#FFD16A` banners with notched ribbon edges, bold sans tally labels, and contrasting black micro-badges for multipliers (e.g., `3X STREAK`).