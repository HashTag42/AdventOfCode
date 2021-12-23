using System.Collections.Generic;   // Required to use the List class.

/// This class represents a list of caves a user can traverse through.
class CavePath
{
    /// This property stores the caves in the path.
    public List<Cave> Caves { get; private set; }

    /// This method allows for the addition of a cave at the end of the path.
    public void Push(Cave Cave) => this.Caves.Add(Cave);

    /// This method allows for the removal of the last cave in the path.
    public void Pop() => this.Caves.RemoveAt(this.Caves.Count - 1);

    /// Default constructor to initialize objects.
    public CavePath() => this.Caves = new List<Cave>();

    /// This constructor initializes the object with a specific cave at the start.
    public CavePath(Cave StartCave) => this.Push(StartCave);

    /// This constructor initializes the object with a spefic list of caves.
    public CavePath(List<Cave> Caves) => this.Caves = Caves;

    /// This override method provides a string representation of the object.
    public override string ToString()
    {
        string output = null;
        foreach(Cave cave in this.Caves)
        {
            output += cave.Name + ",";
        }
        // Remove that last comma before returning:
        return output.Remove(output.Length - 1);
    }

}