// 코딩테스트 연습 > 연습문제 > 달리기 경주
// 2024-10-31
// with ChatGPT

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        // String, Integer 타입의 값만 Map 인터페이스에 사용
        // 제네릭<>: 특정한 자료형만 다루도록 자료형을 미리 지정함
        // HashMap 객체를 생성하여 indexMap에 할당
        Map<String, Integer> indexMap = new HashMap<>();
        // players 배열을 순회하며 선수들의 이름과 현재 위치를 indexMap에 저장
        for (int i = 0; i < players.length; i++) {
            indexMap.put(players[i], i);            // 선수들의 이름과 인덱스(i)
        }

        // 추월한 선수의 이름을 키로 하여 HashMap에서 현재 위치를 조회
        for (String name : callings) {
            int currentIndex = indexMap.get(name);  // .get: 해당 키에 연결된 값을 반환
            if (currentIndex > 0) {
                // 현재 선수(name)와 바로 앞의 선수(frontPlayer)의 위치를 교환
                String frontPlayer = players[currentIndex - 1];
                players[currentIndex - 1] = name;
                players[currentIndex] = frontPlayer;

                // 위치가 변경된 두 선수를 해시 맵에 업데이트
                indexMap.put(name, currentIndex - 1);
                indexMap.put(frontPlayer, currentIndex);
            }
        }
        return players;
    }
}