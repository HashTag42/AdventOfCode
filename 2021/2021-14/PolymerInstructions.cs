using System.Collections.Generic;

public class PolymerInstructions
{
    public string Template { get; init; }
    public List<InsertionRule> InsertionRules { get; init; }

    public int Count => this.InsertionRules.Count;

    public PolymerInstructions(string[] Lines)
    {
        Template = Lines[0];

        InsertionRules = new List<InsertionRule>();

        for(int l = 2; l < Lines.GetLength(0); l++)
        {
            InsertionRules.Add(new InsertionRule(Lines[l]));
        }
    }
}
