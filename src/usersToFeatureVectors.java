import java.io.*;
import java.util.HashMap;


public class usersToFeatureVectors {
	static int UNIQUESONGS = 384546;
	static int UNIQUEUSERS = 1019318;
	static int USERIDINDEX = 0;
	static int SONGIDINDEX = 1;
	static int PLAYCOUNTINDEX = 2;
	static int USERLIMIT = 100000;
	
	public static void main(String[] args) throws IOException {
		int selected = createVectors();
		while(selected != 0) {
			selected = createVectors();
		}

	}
	
	public static int createVectors() throws IOException {
		HashMap<String, HashMap<Integer, Integer>> userFeatureHash = new HashMap<String, HashMap<Integer,Integer>>();
		HashMap<String, Integer> songHash = readSongIndexes();
		HashMap<String, Integer> selectedUsersHash = new HashMap<String, Integer>();
		HashMap<String, Integer> finishedUsersHash = new HashMap<String, Integer>();
		
		
		int indexAssigner = 0;
    	int selected = 0;
		
		BufferedReader br = new BufferedReader(new FileReader("train_triplets.txt"));
		BufferedReader brSelector = new BufferedReader(new FileReader("uniqueUsers.txt"));
		BufferedReader brAlreadyFinished = new BufferedReader(new FileReader("finishedUsers.txt"));
		
		BufferedWriter bw = new BufferedWriter(new FileWriter("userFeatureVectors.txt",true));
		BufferedWriter bwFinished = new BufferedWriter(new FileWriter("finishedUsers.txt", true));
		
		//IO Code to read in already finished users
		try {
	        String line = brAlreadyFinished.readLine();
	        while (line != null) {
	        	finishedUsersHash.put(line, 0);
	        	line = brAlreadyFinished.readLine();
	        }
		} finally {
	        brAlreadyFinished.close();
	    }
		
		//IO code to select the next USERLIMIT users to create feature vectors for
		try {
	        String line = brSelector.readLine();
	        while (line != null && selected < USERLIMIT) {
	        	String[] tuple = line.split(",");
	        	if(!finishedUsersHash.containsKey(tuple[0])) {
	        		selectedUsersHash.put(tuple[0], 0);
	        		selected++;
	        	}
	        	line = brSelector.readLine();
	        }
		} finally {
	        brSelector.close();
	    }
		
		//IO code to read in play counts for users selected above
	    try {
	        String line = br.readLine();
	
	        while (line != null) {
	        	String[] triplet = line.split("\t"); //triplets are tab seperated
	        	if(selectedUsersHash.containsKey(triplet[USERIDINDEX])) {
	        		if(!userFeatureHash.containsKey(triplet[USERIDINDEX])) {
	        			userFeatureHash.put(triplet[USERIDINDEX], new HashMap<Integer,Integer>());
	        		}
	        		HashMap<Integer, Integer> featureHash = userFeatureHash.get(triplet[USERIDINDEX]);
	        		int songID = songHash.get(triplet[SONGIDINDEX]);
	        		
	        		featureHash.put(songID, Integer.parseInt(triplet[PLAYCOUNTINDEX]));
	        	}
	            line = br.readLine();
	        }
	    } finally {
	        br.close();
	    }
	    
	    //IO code to print user feature vectors to file
	    try {
	    	for(String key : userFeatureHash.keySet()) {
	    		HashMap<Integer,Integer> featureHash = userFeatureHash.get(key);
	    		bw.append(key);
	    		for(Integer songID : featureHash.keySet()) {
	    			bw.append(",(" + songID + "," + featureHash.get(songID) + ")");
	    		}
	    		bw.append("\n");
	    		bwFinished.append(key + "\n");
	    	}
	    } finally {
	    	bw.close();
	    	bwFinished.close();
	    }
	    
	    return selected;
	}
	
	//Method to read in songID mappings
	public static HashMap<String, Integer> readSongIndexes() throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("songIndexMap.txt"));
		HashMap<String, Integer> songMap = new HashMap<String, Integer>();
	    try {
	        String line = br.readLine();
	
	        while (line != null) {
	        	String[] tuple = line.split(",");
	        	songMap.put(tuple[0], Integer.parseInt(tuple[1]));
	            line = br.readLine();
	        }
	    } finally {
	        br.close();
	    }
		
	    return songMap;
	}

}
