#!/bin/bash
# Download Polymarket time-series data for top political markets
# Created: 2026-02-05

DATA_DIR="projects/vibepolitics/data/timeseries"
mkdir -p "$DATA_DIR"

echo "=== Downloading Polymarket Time-Series Data ==="
echo "Date: $(date -u +%Y-%m-%d)"

# Function to fetch price history and save to CSV
fetch_timeseries() {
    local name="$1"
    local token_id="$2"
    local outcome="$3"
    local safe_name=$(echo "$name" | tr ' ' '_' | tr -cd '[:alnum:]_')
    local filename="${DATA_DIR}/${safe_name}_${outcome}.csv"
    
    echo "Fetching: $name ($outcome)..."
    
    # Fetch all history with hourly fidelity
    response=$(curl -s "https://clob.polymarket.com/prices-history?market=${token_id}&interval=max&fidelity=60")
    
    # Check if we got valid data
    count=$(echo "$response" | jq '.history | length' 2>/dev/null)
    
    if [ "$count" -gt 0 ]; then
        # Convert to CSV
        echo "timestamp_unix,timestamp_utc,price" > "$filename"
        echo "$response" | jq -r '.history[] | [.t, (.t | todate), .p] | @csv' >> "$filename"
        echo "  ✓ Saved $count data points to $filename"
    else
        echo "  ✗ No data for $name"
    fi
}

# Get Dem Nominee 2028 top candidates
echo ""
echo "=== Democratic Presidential Nominee 2028 ==="
dem_data=$(curl -s "https://gamma-api.polymarket.com/events?slug=democratic-presidential-nominee-2028")
# Top candidates by activity
fetch_timeseries "DemNom_GretchenWhitmer" "57761428076807364758801249497410455358987881775226117256631754592198558850468" "yes"
fetch_timeseries "DemNom_JoshShapiro" "$(echo "$dem_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Josh Shapiro") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "DemNom_GavinNewsom" "$(echo "$dem_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Gavin Newsom") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "DemNom_AOC" "$(echo "$dem_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Alexandria Ocasio-Cortez") | .clobTokenIds' | jq -r '.[0]')" "yes"

# Fed Chair picks
echo ""
echo "=== Trump Fed Chair Nomination ==="
fed_data=$(curl -s "https://gamma-api.polymarket.com/events?slug=who-will-trump-nominate-as-fed-chair")
fetch_timeseries "FedChair_KevinWarsh" "$(echo "$fed_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Kevin Warsh") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "FedChair_JayPowell" "$(echo "$fed_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Jay Powell") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "FedChair_LarryKudlow" "$(echo "$fed_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Larry Kudlow") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "FedChair_ScottBessent" "$(echo "$fed_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Scott Bessent") | .clobTokenIds' | jq -r '.[0]')" "yes"

# 2028 Presidential Winner
echo ""
echo "=== Presidential Election Winner 2028 ==="
pres_data=$(curl -s "https://gamma-api.polymarket.com/events?slug=presidential-election-winner-2028")
fetch_timeseries "Pres2028_JDVance" "$(echo "$pres_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "JD Vance") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "Pres2028_DonaldTrumpJr" "$(echo "$pres_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Donald Trump Jr") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "Pres2028_GavinNewsom" "$(echo "$pres_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Gavin Newsom") | .clobTokenIds' | jq -r '.[0]')" "yes"

# GOP Nominee 2028
echo ""
echo "=== Republican Presidential Nominee 2028 ==="
gop_data=$(curl -s "https://gamma-api.polymarket.com/events?slug=republican-presidential-nominee-2028")
fetch_timeseries "GOPNom_JDVance" "$(echo "$gop_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "JD Vance") | .clobTokenIds' | jq -r '.[0]')" "yes"
fetch_timeseries "GOPNom_DonaldTrumpJr" "$(echo "$gop_data" | jq -r '.[0].markets[] | select(.groupItemTitle == "Donald Trump Jr.") | .clobTokenIds' | jq -r '.[0]')" "yes"

# Other key markets
echo ""
echo "=== Other Key Markets ==="
# Portugal election
port_data=$(curl -s "https://gamma-api.polymarket.com/events?slug=portugal-presidential-election")
fetch_timeseries "Portugal_GouveiaMelo" "$(echo "$port_data" | jq -r '.[0].markets[] | select(.groupItemTitle | test("Gouveia"; "i")) | .clobTokenIds' | jq -r '.[0]' | head -1)" "yes"

# Fed March decision
fed_march=$(curl -s "https://gamma-api.polymarket.com/events?slug=fed-decision-in-march-885")
fetch_timeseries "FedMarch_NoChange" "$(echo "$fed_march" | jq -r '.[0].markets[] | select(.groupItemTitle == "No change") | .clobTokenIds' | jq -r '.[0]')" "yes"

# Venezuela
ven_data=$(curl -s "https://gamma-api.polymarket.com/events?slug=venezuela-leader-end-of-2026")
fetch_timeseries "Venezuela_Maduro" "$(echo "$ven_data" | jq -r '.[0].markets[] | select(.groupItemTitle | test("Maduro"; "i")) | .clobTokenIds' | jq -r '.[0]')" "yes"

# Russia-Ukraine ceasefire
ceasefire=$(curl -s "https://gamma-api.polymarket.com/events?slug=russia-x-ukraine-ceasefire-by-march-31-2026")
fetch_timeseries "RussiaUkraine_Ceasefire" "$(echo "$ceasefire" | jq -r '.[0].markets[0].clobTokenIds' | jq -r '.[0]')" "yes"

echo ""
echo "=== Download Complete ==="
ls -la "$DATA_DIR"/*.csv 2>/dev/null | wc -l
echo "files downloaded"
