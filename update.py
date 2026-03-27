import codecs

with codecs.open(r"d:\rganandovidas\index.html", "r", "utf-8") as f:
    lines = f.readlines()

def apply_replacement(lines, start, end, new_lines_str):
    new_lines = [(line + "\n") for line in new_lines_str.split("\n")]
    if new_lines and new_lines[-1] == "\n":
        new_lines.pop()
    return lines[:start] + new_lines + lines[end:]

new_css = """        /* ESTADO A: MINI PLAYER BAR */
        .player-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 70px;
            background-color: var(--bg-body);
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 16px;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
            z-index: 50;
            transition: transform 0.3s ease, opacity 0.3s ease;
        }

        .player-bar.hidden {
            transform: translateY(100%);
            opacity: 0;
            pointer-events: none;
        }

        .radio-btn-open {
            background: var(--text-main);
            color: #fff;
            border: none;
            border-radius: 50%;
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }
        .radio-btn-open:active {
            transform: scale(0.95);
        }

        /* ESTADO B: FULL RADIO PLAYER PANEL */
        .radio-panel {
            background: linear-gradient(135deg, #0f172a 0%, #172554 100%);
            border-radius: 20px;
            padding: 24px;
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
            position: relative;
            overflow: hidden;
            max-width: 400px;
            margin: 0 auto;
        }
        
        .radio-panel-close {
            position: absolute;
            top: 16px;
            right: 16px;
            background: rgba(255,255,255,0.1);
            border: none;
            color: #fff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.3s;
        }

        .radio-image-container {
            position: relative;
            width: 180px;
            height: 180px;
            margin: 20px 0 30px 0;
        }

        .radio-image {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #F3BC55;
            position: relative;
            z-index: 2;
            box-shadow: 0 0 20px rgba(243, 188, 85, 0.4);
        }

        /* Sound Wave Animation */
        .sound-wave {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: rgba(243, 188, 85, 0.3);
            z-index: 1;
            opacity: 0;
            transform: scale(1);
        }

        .sound-wave.active {
            animation: pulse-wave 2s infinite ease-out;
        }

        .sound-wave.active:nth-child(2) {
            animation-delay: 0.6s;
        }

        .sound-wave.active:nth-child(3) {
            animation-delay: 1.2s;
        }

        @keyframes pulse-wave {
            0% { transform: scale(1); opacity: 0.8; }
            100% { transform: scale(1.6); opacity: 0; }
        }

        /* Marquee Text */
        .marquee-container {
            width: 100%;
            overflow: hidden;
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
            padding: 8px 0;
            margin-bottom: 24px;
        }

        .marquee-text {
            display: inline-block;
            white-space: nowrap;
            color: #F3BC55;
            font-family: var(--font-title);
            font-weight: 700;
            font-size: 14px;
            animation: marquee 10s linear infinite;
        }

        @keyframes marquee {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }

        /* Full Player Controls */
        .full-controls {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            width: 100%;
            margin-bottom: 20px;
        }

        .full-play-btn {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background: #F3BC55;
            color: #000;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(243, 188, 85, 0.4);
            transition: transform 0.2s, background 0.2s;
        }

        .full-play-btn:active {
            transform: scale(0.95);
        }

        .full-play-btn svg {
            width: 28px;
            height: 28px;
            fill: currentColor;
            margin-left: 4px;
        }
        
        .full-play-btn.playing svg.play-icon { display: none; }
        .full-play-btn.playing svg.pause-icon { display: block; margin-left: 0; }
        
        .full-play-btn:not(.playing) svg.pause-icon { display: none; }
        .full-play-btn:not(.playing) svg.play-icon { display: block; }

        .vol-container {
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
            padding: 0 20px;
        }

        .vol-container svg {
            color: #fff;
            width: 20px;
            height: 20px;
        }

        .full-vol-control {
            flex: 1;
            height: 6px;
            -webkit-appearance: none;
            background: rgba(255,255,255,0.2);
            border-radius: 3px;
            outline: none;
        }
        
        .full-vol-control::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #F3BC55;
            cursor: pointer;
        }"""

new_panel = """        <!-- ESTADO B: RADIO GANANDO VIDAS -->
        <section id="radioganandovidas" class="page">
            <div class="radio-panel">
                <button class="radio-panel-close" onclick="closeRadioPanel()" aria-label="Cerrar">✕</button>
                <div class="radio-image-container">
                    <div class="sound-wave wave-anim"></div>
                    <div class="sound-wave wave-anim"></div>
                    <div class="sound-wave wave-anim"></div>
                    <img src="./screengv.jpg" alt="Radio Ganando Vidas" class="radio-image">
                </div>
                
                <div class="marquee-container">
                    <div class="marquee-text">Ganar Vidas para el reino de DIOS sin Colocar Limites &nbsp; &nbsp; &nbsp; &nbsp; Ganar Vidas para el reino de DIOS sin Colocar Limites</div>
                </div>

                <div class="full-controls">
                    <button class="full-play-btn" id="fullPlayBtn" onclick="toggleAudioFull()" aria-label="Play/Pause">
                        <svg class="play-icon" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                        <svg class="pause-icon" viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>
                    </button>
                </div>

                <div class="vol-container">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                        <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
                    </svg>
                    <input type="range" class="full-vol-control" min="0" max="1" step="0.05" value="1" id="fullVolControl" oninput="changeVolume(this.value)">
                </div>
            </div>
        </section>"""

new_player_bar = """    <!-- ESTADO A: PLAYER BOTTOM BAR -->
    <div class="player-bar" id="playerBar">
        <div class="player-info" style="flex: 1;">
            <div style="display:flex; align-items:center;">
                <span class="live-badge" style="margin-right: 8px;">EN VIVO</span>
                <span style="font-size:15px; font-weight: 700;">Radio Ganando Vidas</span>
            </div>
        </div>
        <button class="radio-btn-open" onclick="switchTab('radioganandovidas')" aria-label="Abrir Radio">
            <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 10a10 10 0 0 1 16 0"></path>
                <path d="M8 14a4 4 0 0 1 8 0"></path>
                <circle cx="12" cy="18" r="2"></circle>
            </svg>
        </button>
    </div>
    <audio id="radioStream" src="https://virtual.multimusic.com.co:8004/stream" preload="none"></audio>"""

new_switch_tab = """            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            const target = document.getElementById(tabId);
            if (target) target.classList.add('active');

            // Handle player bar visibility
            const playerBar = document.getElementById('playerBar');
            if (tabId === 'radioganandovidas') {
                playerBar.classList.add('hidden');
            } else {
                playerBar.classList.remove('hidden');
            }

            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));"""

new_audio_js = """        // Audio logic
        const radio = document.getElementById('radioStream');
        const fullPlayBtn = document.getElementById('fullPlayBtn');

        function toggleAudioFull() {
            if (radio.paused) {
                radio.play().then(() => {
                    fullPlayBtn.classList.add('playing');
                    document.querySelectorAll('.wave-anim').forEach(el => el.classList.add('active'));
                }).catch(e => {
                    console.error(e);
                    alert("Error al conectar. Toque de nuevo.");
                });
            } else {
                radio.pause();
                fullPlayBtn.classList.remove('playing');
                document.querySelectorAll('.wave-anim').forEach(el => el.classList.remove('active'));
            }
        }

        function changeVolume(val) {
            radio.volume = val;
        }

        function closeRadioPanel() {
            // Regresar a la última pestaña, por defecto radio
            switchTab('radio');
        }"""

lines = apply_replacement(lines, 1157, 1187, new_audio_js)
lines = apply_replacement(lines, 1119, 1124, new_switch_tab)
lines = apply_replacement(lines, 1076, 1107, new_player_bar)
lines = apply_replacement(lines, 819, 827, new_panel)
lines = apply_replacement(lines, 290, 403, new_css)

with codecs.open(r"d:\rganandovidas\index.html", "w", "utf-8") as f:
    f.writelines(lines)

print("Modification complete.")
