using System.Collections.Generic;   // List class

class Puzzle {

    public string Title { get; init; }
    public string URL { get; init; }

    public List<PuzzlePart> Parts { get; private set; }

    public override string ToString() => (Title + " [" + URL + "]");

    public Puzzle(string title, string url) {
        Title   = title;
        URL     = url;
        Parts   = new List<PuzzlePart>();
    }

    public bool AddPuzzlePart(PuzzlePart PuzzlePart) {
        Parts.Add(PuzzlePart);
        return true;
    }
}