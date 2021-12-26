class DefaultDict {
    private Dictionary<string, List<string>> dic { get; set; }

    public DefaultDict() => this.dic = new Dictionary<string, List<string>>();

    public void Add(string Key, string Value)
    {
        if(!dic.ContainsKey(Key)) {
            List<string> empty = new List<string>();
            dic.Add(Key, empty);
        }
        List<string> values;
        if(dic[Key] != null) {
            values = dic[Key];
        } else {
            values = new List<string>();
        }
        values.Add(Value);
        dic[Key] = values;
    }

    public List<string> GetValues(string Key) {
        List<string> values;
        if(dic[Key] != null) {
            values = dic[Key];
        } else {
            values = new List<string>();
        }
        return values;
    }

}