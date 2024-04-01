<script lang="ts">
  let isDragOver: boolean = false;
  let fileInput: HTMLInputElement;
  let uploadedFile: File | null = null;

  function handleFileChange(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      uploadedFile = input.files[0];
      uploadFile();
    }
  }

  async function uploadFile() {
    if (!uploadedFile) return;

    const formData = new FormData();
    formData.append("file", uploadedFile);

    try {
      const response = await fetch("/remove-bg", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const blob = await response.blob();
        downloadFile(blob, uploadedFile.name);
      } else {
        console.error("File upload failed");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  function downloadFile(blob: Blob, fileName: string) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    // a.click();
    // window.URL.revokeObjectURL(url);
    // a.remove();
  }

  function handleDrop(event: DragEvent) {
    event.preventDefault();
    isDragOver = false;
    if (event.dataTransfer?.files[0]) {
      uploadedFile = event.dataTransfer.files[0];
      uploadFile();
    }
  }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<section
  class="drop-zone"
  class:dragover={isDragOver}
  on:click={() => fileInput.click()}
  on:dragover|preventDefault={() => (isDragOver = true)}
  on:dragleave={() => (isDragOver = false)}
  on:drop={handleDrop}
>
  <h1>rmbg</h1>
  <input type="file" id="fileInput" name="file" bind:this={fileInput} on:change={handleFileChange} hidden />
</section>

<style>
  .drop-zone {
    border: 2px dashed #ccc;
    padding: 20px;
    width: 50vw;
    height: 50vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }

  .drop-zone.dragover {
    background-color: #f0f0f0;
  }
</style>
