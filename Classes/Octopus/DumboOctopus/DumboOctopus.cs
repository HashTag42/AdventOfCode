using System;   // ArgumentOutOfRangeException

class DumboOctopus // : Octopus
{
    public int Energy { get; private set; }

    public bool IsFlashing { get; private set; }

    public DumboOctopus(int Energy)
    {
        if(Energy < 0 || Energy > 9) {
            throw new ArgumentOutOfRangeException();
        }
        else {
            this.Energy= Energy;
            this.IsFlashing= (0 == Energy) ? true : false;
        }
    }

    public void Step()
    {
        Energy++;
        if(10 == Energy)
        {
            Energy= 0;
            IsFlashing= true;
        }
    }

    public void StopFlashing()
    {
        IsFlashing= false;
    }

    public override string ToString()
    {
        return (Energy.ToString());
    }
}