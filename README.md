<h1 align="center">🎸 myPyGuitar</h1>
<p align="center">Air Guitar using Hand Gestures & Real-time Audio Chords</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/OpenCV-%3E%3D4.0-orange" />
  <img src="https://img.shields.io/badge/MediaPipe-Hands-red" />
</p>

<hr />

<h2>✨ Features</h2>
<ul>
  <li>🎵 Play guitar chords in the air using your fingers</li>
  <li>🖐️ Real-time hand tracking via MediaPipe</li>
  <li>🔊 Major chord sounds using Pygame</li>
  <li>🧠 Intelligent gesture-to-chord mapping</li>
  <li>🎥 Live webcam feed with chord overlay</li>
</ul>

<h2>🧠 Gesture to Chord Mapping</h2>

<table>
  <tr>
    <th>Gesture</th>
    <th>Fingers Shown</th>
    <th>Chord Played</th>
  </tr>
  <tr>
    <td>👆</td>
    <td>1</td>
    <td>C Major</td>
  </tr>
  <tr>
    <td>✌️</td>
    <td>2</td>
    <td>D Major</td>
  </tr>
  <tr>
    <td>🤟</td>
    <td>3</td>
    <td>E Major</td>
  </tr>
  <tr>
    <td>🖖</td>
    <td>4</td>
    <td>F Major</td>
  </tr>
  <tr>
    <td>🖐️</td>
    <td>5</td>
    <td>G Major</td>
  </tr>
  <tr>
    <td>👍</td>
    <td>Thumbs Up</td>
    <td>B Major</td>
  </tr>
</table>

<h2>🚀 Getting Started</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/satyanweshi11/myPyGuitar.git</code></pre>
  </li>
  <li>Create a virtual environment (optional but recommended):
    <pre><code>python -m venv env</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Run the application:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

<h2>📁 Folder Structure</h2>

<pre>
myPyGuitar/
│
├── assets/
│   └── sounds/              # Major chord sound files (.wav)
├── hand_tracking.py         # Detects fingers using MediaPipe
├── chord_manager.py         # Maps finger count to chords
├── sound_manager.py         # Handles sound logic (if used separately)
├── main.py                  # Main application logic
├── requirements.txt         # Python dependencies
└── .gitignore               # Ignore virtual env & pycache
</pre>

<h2>💡 Note</h2>

<p>
⚠️ Avoid committing your <code>env/</code> folder or large binaries (like DLLs) to GitHub. Use <code>.gitignore</code> properly.<br />
If you run into large file errors, use <a href="https://git-lfs.github.com/">Git LFS</a> or remove the files from the repo.
</p>

<h2>🛠️ Built With</h2>
<ul>
  <li><a href="https://opencv.org/">OpenCV</a> - For image & webcam feed</li>
  <li><a href="https://mediapipe.dev/">MediaPipe Hands</a> - For finger tracking</li>
  <li><a href="https://www.pygame.org/">Pygame</a> - For sound playback</li>
</ul>

<h2>🙌 Contribution</h2>
<p>Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>📜 License</h2>
<p>This project is <b>open-source</b> and free to use under the <code>MIT License</code>.</p>
