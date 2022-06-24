function extractFile (path) {
    // MasK
    let file = path.split('\\')[path.split('\\').length - 1].split('.');
    let fileName = file.slice(0, file.length -1).join('.');
    let fileExt = file[file.length - 1];

    console.log(`File name: ${fileName}`);
    console.log(`File extension: ${fileExt}`);
}

extractFile('C:\\Internal\\training-internal\\Template.pptx');