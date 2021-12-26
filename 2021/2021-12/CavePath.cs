using System.Collections.Generic;   // Required to use the List class.

/// This class represents a list of caves a user can traverse through.
class CavePath
{
    /// This property stores the caves in the path.
    public List<CaveNode> CaveNodes { get; private set; }

    /// This method allows for the addition of a cave at the end of the path.
    public void Push(CaveNode CaveNode) => this.CaveNodes.Add(CaveNode);

    /// This method allows for the removal of the last cave in the path.
    public void Pop() => this.CaveNodes.RemoveAt(this.CaveNodes.Count - 1);

    /// Default constructor to initialize objects.
    public CavePath() => this.CaveNodes = new List<CaveNode>();

    /// This constructor initializes the object with a specific cave at the start.
    public CavePath(CaveNode StartCaveNode) : this() => this.Push(StartCaveNode);

    /// This constructor initializes the object with a spefic list of caves.
    public CavePath(List<CaveNode> CaveNodes) => this.CaveNodes = CaveNodes;

    /// This override method provides a string representation of the object.
    public override string ToString()
    {
        string output = null;
        string separator = ",";

        foreach(CaveNode caveNode in this.CaveNodes)
        {
            output += caveNode.Name + separator;
        }
        // Remove the trailing separator
        output = output.Substring(0, output.Length - separator.Length);

        return output;
    }

}