public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
            String encodedStr = "";
    for (String str : strs) {
        encodedStr = encodedStr + str.length() + "#" + str;
    }
    return encodedStr;

    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> list = new ArrayList<>();
        for (int startIndex = 0; startIndex < s.length();) {
            int idx = s.indexOf("#", startIndex);
            int numOfChars = Integer.parseInt(s.substring(startIndex, idx));
            list.add(s.substring(idx+1, idx+1+numOfChars));
            startIndex = idx+1+numOfChars;
        }
    return list;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));