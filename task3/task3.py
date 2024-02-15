from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello SKAI Labs!"

#function that determines what is the maximum number of interviews
def maxAlgo(start_times, end_times):
    '''
    The algorithm sorts interviews based on their starting times. Then, it determines how many interviews will be excluded 
    after each interview starts and puts those values in the 'excluding' array. Next, it iterates through the 'excluding' array 
    and checks every element against the currently best option. If the current element is better than the current best option, 
    then the current element becomes the best option. If not, then we move on to the next element until we reach a point 
    where no further exclusions occur (i.e., when the interview is completed and no longer overlaps with others).

    We determine which option is better by comparing how many more interviews would be excluded if we chose either option.
    EXP: option A excludes 3 more interviews, option B excludes 1 interview and curent best option which we would have to miss
    in order to attend this one = 2; which means option B is better.
    '''
    excluding =[] # the exluded interviews array

    #sorting both lists based on values in start_times, basically sorting as pairs
    start_times_sorted = list(set(start_times))
    start_times_sorted.sort()
    end_times_sorted = []
    for i in start_times_sorted:
        for j in range(0, len(start_times)):
            if(start_times[j] == i):
                end_times_sorted.append(end_times[j])
    
    #determines if interview at index x is chosen, how many interviews will be excluded after it
    for x in range(0,len(start_times)):
        for y in range(x+1, len(start_times)):
            if end_times_sorted[x]<=start_times_sorted[y]:
                excluding.append(y-x-1)
                break
    excluding.append(0) #last interview won't exlude any other interview
    
    max=0 #number of interviews that will be returned as the result
    last=-1 # last best option
    for interview in excluding:
        if last == 0:
            max = max +1 #if last best option expiered; we are taking that interview
        if last == -1:
            last = interview #initial setup
        elif last > interview:
            last = interview #if current option is better than last option
        else: #if not decrease the exluding number of best option, since we are moving forward
            last = last -1
            if last < 0:
                last=0
    if last == 0: #we do not check last interview in the loop so we do it outside
            max = max +1
    return max

########TASK ENDPOINT#######
@app.route("/task", methods=["POST"])
def task():
    #checks if request body has all the elements needed, and checks if the 2 arrays are same length
    if not request.json or "start_times" not in request.json or "end_times" not in request.json or len(request.json["start_times"])!= len(request.json["end_times"]):
        return jsonify({"error": "Bad Request"}), 400

    start_times=request.json["start_times"]
    end_times=request.json["end_times"]
    max_interviews = maxAlgo(start_times, end_times)

    response = {"max_interviews": max_interviews}
    return jsonify(response), 200

if __name__ == "__main__":  
   app.run()