# 5G-Registration-Attack

### README

# Registration Time Analysis for UE using Pyshark

This project contains a Python script that analyzes a pcap (packet capture) file to find out the time it takes for a User Equipment (UE) to register. The script uses the `pyshark` library to read the pcap file and `pandas` to process and store the results.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- `pyshark` library
- `pandas` library
- Wireshark (for capturing the pcap file)

You can install the required Python libraries using pip:
```sh
pip install pyshark pandas
```

## Usage

1. **Capture Network Traffic:**
   - Use Wireshark or any other network capturing tool to capture the traffic and save it as a `.pcap` file.
   
2. **Place the pcap File:**
   - Place the `.pcap` file in the same directory as the script or update the `pcap_file` path variable in the script.

3. **Run the Script:**
   - Execute the script to analyze the pcap file and calculate the registration times.
   ```sh
   python find_reg_time.py
   ```

## Script Details

### `find_reg_time.py`

This script processes the pcap file to calculate the time differences between the registration attempts of UEs. Below is the breakdown of the script:

```python
import pyshark
import pandas as pd
from collections import defaultdict

def analyze_pcap(pcap_file):
    # Load the pcap file
    capture = pyshark.FileCapture(pcap_file, display_filter='ngap')

    # Dictionary to store packets by ngap.RAN_UE_NGAP_ID
    packets_by_id = defaultdict(list)

    # Iterate through each packet in the capture
    for packet in capture:
        try:
            # Check if the packet contains ngap layer
            if hasattr(packet, 'ngap'):
                # Debug: Print packet details
                print(f"Packet: {packet}")

                # ngap.RAN_UE_NGAP_ID can be a list if multiple values exist
                ran_ue_ngap_ids = packet.ngap.get_field('ran_ue_ngap_id')

                # Debug: Print RAN_UE_NGAP_ID values
                print(f"RAN_UE_NGAP_IDs: {ran_ue_ngap_ids}")

                # If the field is not a list, convert it to a list
                if not isinstance(ran_ue_ngap_ids, list):
                    ran_ue_ngap_ids = [ran_ue_ngap_ids]

                for ran_ue_ngap_id in ran_ue_ngap_ids:
                    ran_ue_ngap_id = int(ran_ue_ngap_id)
                    if 1 <= ran_ue_ngap_id <= 1000:
                        # Append the packet sniff time to the corresponding ID list
                        packets_by_id[ran_ue_ngap_id].append(packet.sniff_time)

        except AttributeError as e:
            # Debug: Print error details
            print(f"Error processing packet: {e}")
            # Skip packets that do not have the required field
            continue
        except Exception as e:
            # Debug: Print unexpected error details
            print(f"Unexpected error: {e}")
            continue

    # List to store the results
    results = []

    # Calculate the highest time difference for each ID
    for ran_ue_ngap_id, times in packets_by_id.items():
        if len(times) > 1:
            max_time = max(times)
            min_time = min(times)
            time_diff = (max_time - min_time).total_seconds()
            results.append((ran_ue_ngap_id, time_diff))

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=['RAN_UE_NGAP_ID', 'Max_Time_Difference'])

    # Save the DataFrame to a CSV file
    df.to_csv('time_differences_ninejun.csv', index=False)

    # Debug: Print DataFrame
    print(df)

# Path to the pcap file
pcap_file = 'fifteenjun.pcap'

# Analyze the pcap file
analyze_pcap(pcap_file)
```

### Output

The script generates a CSV file (`time_differences_ninejun.csv`) containing the maximum time differences for each RAN_UE_NGAP_ID.

### CSV File Structure
The CSV file contains the following columns:
- `RAN_UE_NGAP_ID`: The unique identifier for the UE.
- `Max_Time_Difference`: The maximum time difference (in seconds) between registration attempts for the corresponding UE.

## Troubleshooting

- Ensure the pcap file contains NGAP packets with `RAN_UE_NGAP_ID` fields.
- Check for dependencies and install missing libraries using pip.



## Author

- [Anurag K Sharma]
- mcs222071

Feel free to reach out if you have any questions or need further assistance.
