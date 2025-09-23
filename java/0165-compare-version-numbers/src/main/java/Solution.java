class Solution {
    public int compareVersion(String version1, String version2) {
        String[] parts1 = version1.split("\\.");
        String[] parts2 = version2.split("\\.");
        int len1 = parts1.length;
        int len2 = parts2.length;
        int minLen = Math.min(len1, len2);
        int i = 0;
        for (; i < minLen; i++) {
            int v1 = Integer.parseInt(parts1[i]);
            int v2 = Integer.parseInt(parts2[i]);
            if (v1 > v2) {
                return 1;
            } else if (v2 > v1) {
                return -1;
            } else {
                // pass
            }
        }
        // need to check if extra revisions are not 0
        if (len1 > len2) {
            while (i < len1) {
                int v1 = Integer.parseInt(parts1[i]);
                if (v1 > 0) {
                    return 1;
                }
                i++;
            }
            
        } else if (len2 > len1) {
            while (i < len2) {
                int v2 = Integer.parseInt(parts2[i]);
                if (v2 > 0) {
                    return -1;
                }
                i++;
            }
        }
        return 0;
    }
}
