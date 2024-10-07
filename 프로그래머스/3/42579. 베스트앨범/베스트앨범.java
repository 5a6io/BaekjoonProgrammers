import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> cnt = new HashMap<>();
        Map<String, HashMap<Integer, Integer>> album = new HashMap<>();
        
        for(int i = 0; i < genres.length; i++){
            if(!cnt.containsKey(genres[i])){
                HashMap<Integer, Integer> m = new HashMap<>();
                m.put(i, plays[i]);
                album.put(genres[i], m);
                cnt.put(genres[i], plays[i]);
            } else {
                album.get(genres[i]).put(i, plays[i]);
                cnt.put(genres[i], cnt.get(genres[i]) + plays[i]);
                
            }
        }
        
        List<String> keySet = new ArrayList<>(cnt.keySet());
        keySet.sort((o1, o2) -> cnt.get(o2) - (cnt.get(o1)));
        List<Integer> answer = new ArrayList();
        
        for(String i : keySet) {
            HashMap<Integer, Integer> map = album.get(i);
            List<Integer> key = new ArrayList(map.keySet());
            
            key.sort((o1, o2) -> map.get(o2) - (map.get(o1)));
            
            answer.add(key.get(0));
            if(key.size() > 1)
                answer.add(key.get(1));
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}