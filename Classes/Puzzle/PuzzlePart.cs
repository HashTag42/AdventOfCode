using System.Collections.Generic;   // List class

class PuzzlePart {

    public string Title { get; init; }
    public string Prompt { get; init; }

    public List<InputAnswerPair> InputsAndAnswers { get; set; }

    public override string ToString() => (Title + ": " + Prompt);
    public PuzzlePart(string Title, string Prompt) {
        this.Title = Title;
        this.Prompt = Prompt;
    }

}
