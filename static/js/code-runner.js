(function () {
  "use strict";

  let pyodideInstance = null;
  let loadingPromise = null;

  async function getPyodide() {
    if (pyodideInstance) return pyodideInstance;
    if (loadingPromise) return loadingPromise;

    loadingPromise = (async () => {
      try {
        document.querySelectorAll(".code-runner-status").forEach(el => {
          el.textContent = "Loading Python runtime...";
          el.className = "code-runner-status loading";
        });

        const script = document.createElement("script");
        script.src = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";
        script.crossOrigin = "anonymous";
        document.head.appendChild(script);

        await new Promise((resolve, reject) => {
          script.onload = resolve;
          script.onerror = () => reject(new Error("Failed to load Pyodide script"));
        });

        pyodideInstance = await globalThis.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/",
        });

        document.querySelectorAll(".code-runner-status").forEach(el => {
          el.textContent = "Ready!";
          el.className = "code-runner-status ready";
          setTimeout(() => { el.textContent = ""; el.className = "code-runner-status"; }, 2000);
        });

        return pyodideInstance;
      } catch (err) {
        document.querySelectorAll(".code-runner-status").forEach(el => {
          el.textContent = "Failed to load: " + err.message;
          el.className = "code-runner-status error";
        });
        throw err;
      }
    })();

    return loadingPromise;
  }

  async function runCode(textarea, outputEl, runBtn) {
    const code = textarea.value.trim();
    if (!code) {
      outputEl.textContent = "Enter some Python code to run.";
      return;
    }

    runBtn.disabled = true;
    runBtn.textContent = "Running...";
    outputEl.textContent = "Running...";
    outputEl.className = "code-runner-output";

    try {
      const pyodide = await getPyodide();

      // Step 1: Redirect stdout to a Python list for capturing
      await pyodide.runPythonAsync(`
import sys
_output_lines = []
class _Capture:
    def write(self, text):
        _output_lines.append(text)
    def flush(self):
        pass
sys.stdout = _Capture()
      `);

      // Step 2: Run the user's code
      await pyodide.runPythonAsync(code);

      // Step 3: Retrieve captured output from Python list
      const lines = pyodide.globals.get("_output_lines");
      let result = "";
      if (lines) {
        for (let i = 0; i < lines.length; i++) {
          result += lines.get(i);
        }
      }

      // Step 4: Restore stdout and clean up
      await pyodide.runPythonAsync(`
sys.stdout = sys.__stdout__
del _output_lines
      `);

      const display = result || "Code executed successfully (no output).";
      outputEl.textContent = display;
      outputEl.className = "code-runner-output success";
    } catch (err) {
      outputEl.textContent = err.message;
      outputEl.className = "code-runner-output error";
    } finally {
      runBtn.disabled = false;
      runBtn.textContent = "Run Code";
    }
  }

  function initRunners() {
    document.querySelectorAll(".code-runner").forEach(runner => {
      const textarea = runner.querySelector(".code-runner-textarea");
      const runBtn = runner.querySelector(".code-runner-btn");
      const outputEl = runner.querySelector(".code-runner-output");

      if (!textarea || !runBtn || !outputEl) return;

      runBtn.addEventListener("click", function (e) {
        e.preventDefault();
        runCode(textarea, outputEl, runBtn);
      });

      textarea.addEventListener("keydown", function (e) {
        if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
          e.preventDefault();
          runCode(textarea, outputEl, runBtn);
        }
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initRunners);
  } else {
    initRunners();
  }
})();