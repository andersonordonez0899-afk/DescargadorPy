const elements = {
  form: document.querySelector("#download-form"),
  input: document.querySelector("#video-url"),
  info: document.querySelector("#video-info"),
  thumbnail: document.querySelector("#video-thumbnail"),
  title: document.querySelector("#video-title"),
  uploader: document.querySelector("#video-uploader"),
  duration: document.querySelector("#video-duration"),
  platform: document.querySelector("#video-platform"),
  formats: document.querySelector("#video-formats"),
  downloadButton: document.querySelector("#download-button"),
};

const submitButton = elements.form.querySelector("button");

let currentVideoUrl = "";

// Utilidades

function formatDuration(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const remainingSeconds = seconds % 60;

  if (hours > 0) {
    return `${hours}:${String(minutes).padStart(2, "0")}:${String(
      remainingSeconds,
    ).padStart(2, "0")}`;
  }

  return `${minutes}:${String(remainingSeconds).padStart(2, "0")}`;
}

// Interfaz

function showFormats(formats) {
  elements.formats.innerHTML = "";

  formats.forEach((format) => {
    const item = document.createElement("li");

    const label = document.createElement("label");

    const radio = document.createElement("input");

    radio.type = "radio";
    radio.name = "format";
    radio.value = format.format_id;

    label.appendChild(radio);
    label.append(` ${format.resolution} (${format.extension})`);

    item.appendChild(label);

    elements.formats.appendChild(item);
  });
}

function getSelectedFormat() {
  const selected = document.querySelector('input[name="format"]:checked');
  if (!selected) {
    throw new Error("Selecciona un formato.");
  }
  return selected.value;
}

function showVideoInfo(video) {
  elements.info.classList.remove("d-none");

  elements.thumbnail.src = video.thumbnail;
  elements.thumbnail.alt = video.title;

  elements.title.textContent = video.title;
  elements.uploader.textContent = video.uploader;
  elements.duration.textContent = formatDuration(video.duration);
  elements.platform.textContent = video.platform;

  showFormats(video.formats);
}

// API

async function getVideoInformation(url) {
  const response = await fetch("/download/info", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      url,
    }),
  });

  if (!response.ok) {
    throw new Error("Error al obtener la información del video.");
  }

  return await response.json();
}

// Eventos

elements.form.addEventListener("submit", async (event) => {
  event.preventDefault();

  submitButton.disabled = true;
  submitButton.textContent = "Cargando...";

  try {
    const url = elements.input.value.trim();

    if (!url) {
      throw new Error("Debes ingresar una URL.");
    }

    currentVideoUrl = url;

    const video = await getVideoInformation(url);

    //console.log(video);

    showVideoInfo(video);
  } catch (error) {
    console.error(error);
    alert(error.message);
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = "Obtener información";
  }
});
elements.downloadButton.addEventListener("click", async () => {
  try {
    const formatId = getSelectedFormat();
    console.log("URL:", currentVideoUrl);
    console.log("Formato:", formatId);
  } catch (error) {
    alert(error.message);
  }
});
