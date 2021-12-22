using System.Collections.Generic;   // List class

class CavePath
{
    private List<Cave> CaveList { get; set; }

    public CavePath()
    {
        this.CaveList = new List<Cave>();
    }

    public CavePath(Cave StartCave) : this()
    {
        this.Push(StartCave);
    }

    public void Push(Cave Cave) => this.CaveList.Add(Cave);

    public void Pop() => this.CaveList.RemoveAt(this.CaveList.Count - 1);

    public override string ToString()
    {
        string output = null;

        foreach(Cave cave in this.CaveList)
        {
            output += cave.Name + ",";
        }
        // Remove that last comma
        output = output.Remove(output.Length - 1);

        return output;
    }

}