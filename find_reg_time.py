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
