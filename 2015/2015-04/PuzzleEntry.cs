class PuzzleEntry {
    public string Input { get; set; }

    public int NumberOfZeros { get; set; }
    public int ExpectedAnswer { get; set; }

    public PuzzleEntry(string inInput, int inNumberOfZeros, int inAnswer) {
        Input = inInput;
        NumberOfZeros = inNumberOfZeros;
        ExpectedAnswer = inAnswer;
    }

    public bool IsAnswer(int inAnswer) {
        return (ExpectedAnswer == inAnswer);
    }

    public string result(int inAnswer) {
        string message = null;
        message += this.IsAnswer(inAnswer) ? "PASS: " : "FAIL: ";
        message += "Input(s): " + this.Input + ", " + this.NumberOfZeros;
        message += " // Answer: " + inAnswer;
        message += " // Expected: " + this.ExpectedAnswer;
        return message;
    }
}
