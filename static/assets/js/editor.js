document.addEventListener("DOMContentLoaded", function () {
    console.log("Editor Script Loaded!");

    const postInput = document.getElementById("postInput");
    const postPreview = document.getElementById("postPreview");

    const boldBtn = document.querySelector(".bi-type-bold").parentElement;
    const italicBtn = document.querySelector(".bi-type-italic").parentElement;
    const bulletBtn = document.querySelector(".bi-list-ul").parentElement;
    const orderedBtn = document.querySelector(".bi-list-ol").parentElement;
    const undoBtn = document.querySelector(".bi-arrow-counterclockwise").parentElement;
    const redoBtn = document.querySelector(".bi-arrow-clockwise").parentElement;

    let undoStack = [];
    let redoStack = [];

    function saveState() {
        undoStack.push(postInput.value);
        redoStack = [];
    }

    function restoreState(stack) {
        if (stack.length > 0) {
            redoStack.push(postInput.value);
            postInput.value = stack.pop();
            updatePreview();
        }
    }

    function updatePreview() {
        postPreview.innerText = postInput.value;
    }

    function convertToUnicode(text, type) {
        const boldMap = { "A": "𝗔", "B": "𝗕", "C": "𝗖", "D": "𝗗", "E": "𝗘", "F": "𝗙", "G": "𝗚", "H": "𝗛", "I": "𝗜", "J": "𝗝", "K": "𝗞", "L": "𝗟", "M": "𝗠", "N": "𝗡", "O": "𝗢", "P": "𝗣", "Q": "𝗤", "R": "𝗥", "S": "𝗦", "T": "𝗧", "U": "𝗨", "V": "𝗩", "W": "𝗪", "X": "𝗫", "Y": "𝗬", "Z": "𝗭", "a": "𝗮", "b": "𝗯", "c": "𝗰", "d": "𝗱", "e": "𝗲", "f": "𝗳", "g": "𝗴", "h": "𝗵", "i": "𝗶", "j": "𝗷", "k": "𝗸", "l": "𝗹", "m": "𝗺", "n": "𝗻", "o": "𝗼", "p": "𝗽", "q": "𝗾", "r": "𝗿", "s": "𝘀", "t": "𝘁", "u": "𝘂", "v": "𝘃", "w": "𝘄", "x": "𝘅", "y": "𝘆", "z": "𝘇" };
        const italicMap = { "A": "𝘈", "B": "𝘉", "C": "𝘊", "D": "𝘋", "E": "𝘌", "F": "𝘍", "G": "𝘎", "H": "𝘏", "I": "𝘐", "J": "𝘑", "K": "𝘒", "L": "𝘓", "M": "𝘔", "N": "𝘕", "O": "𝘖", "P": "𝘗", "Q": "𝘘", "R": "𝘙", "S": "𝘚", "T": "𝘛", "U": "𝘜", "V": "𝘝", "W": "𝘞", "X": "𝘟", "Y": "𝘠", "Z": "𝘡", "a": "𝘢", "b": "𝘣", "c": "𝘤", "d": "𝘥", "e": "𝘦", "f": "𝘧", "g": "𝘨", "h": "𝘩", "i": "𝘪", "j": "𝘫", "k": "𝘬", "l": "𝘭", "m": "𝘮", "n": "𝘯", "o": "𝘰", "p": "𝘱", "q": "𝘲", "r": "𝘳", "s": "𝘴", "t": "𝘵", "u": "𝘶", "v": "𝘷", "w": "𝘸", "x": "𝘹", "y": "𝘺", "z": "𝘻" };
        
        return text.split("").map(char => type === "bold" ? boldMap[char] || char : italicMap[char] || char).join("");
    }

    function formatText(type) {
        saveState();
        const start = postInput.selectionStart;
        const end = postInput.selectionEnd;
        const selectedText = postInput.value.substring(start, end);
        
        if (!selectedText) return;

        const formattedText = convertToUnicode(selectedText, type);
        postInput.setRangeText(formattedText, start, end, "end");
        updatePreview();
    }

    function addListMarker(marker) {
        saveState();
        const lines = postInput.value.split("\n");
        const start = postInput.selectionStart;
        const end = postInput.selectionEnd;

        let newText = "";
        let insideSelection = false;

        for (let i = 0; i < lines.length; i++) {
            const lineStart = newText.length;
            const lineEnd = newText.length + lines[i].length;

            if (lineStart >= start && lineEnd <= end) {
                insideSelection = true;
            }

            if (insideSelection && lines[i].trim() !== "") {
                newText += marker + " " + lines[i] + "\n";
            } else {
                newText += lines[i] + "\n";
            }

            if (lineEnd >= end) {
                insideSelection = false;
            }
        }

        postInput.value = newText.trim();
        updatePreview();
    }

    boldBtn.addEventListener("click", () => formatText("bold")); // LinkedIn Bold
    italicBtn.addEventListener("click", () => formatText("italic")); // LinkedIn Italic
    bulletBtn.addEventListener("click", () => addListMarker("•")); // LinkedIn Bullet List
    orderedBtn.addEventListener("click", () => addListMarker("1.")); // LinkedIn Ordered List
    undoBtn.addEventListener("click", () => restoreState(undoStack));
    redoBtn.addEventListener("click", () => restoreState(redoStack));

    postInput.addEventListener("input", updatePreview);
});
