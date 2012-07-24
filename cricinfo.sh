output=$(curl -s http://www.espncricinfo.com/sri-lanka-v-india-2012/engine/current/match/564782.html | sed -nr 's/.*<title>(.*?)<\/title>.*/\1/p' )

Player_score=$( echo "$output" | awk -F "(" '{sub(/\)/,""); print $2}' | awk -F"|" '{print $1}')

echo "$Player_score"

Team_score=$(echo "$output" | awk -F"(" '{print $1}')
echo "$Team_score"

