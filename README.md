# 🌍 DataExtractorSuite - AI Assistant

This suite is geared towards efficiently extracting data to be used in the development of an AI Assistant powered by AzureML, Promptflow, and more notably, the LLM (based on GPT-4). Post extraction, these datasets will undergo embedding processing with `text-embedding-ada-002` and will be stored within a Cognitive Search environment for enhanced accessibility and search capabilities.

### 📜 Usage

1. Pour your data into the `data/map_data.json` file.
2. Light up the main function to see your data transformed into markdown:
    ```bash
    python map_data_processor.py
    ```

## 📦 Functions & Features

- **DataExtractor**: The primary pivot around which the extraction logic revolves. It filters, processes, and saves the data, making extraction seamless.
- **accommodation_extract**: Distils details of accommodations.
- **pharmacy_extract**: Hones in on pharmacy specifics.
- **gathering_extract**: Sifts through gathering point data.
- **vet_extract**: Focuses on veterinarians and their practices.
- **food_extract**: Whisks through food joint data.
- **hospital_extract**: Operates on hospital details.
- **evacuation_extract**: Unearths details of evacuation points.

## 📝 Note

This suite is an embodiment of versatility and can be recalibrated according to the nuances of your data. For those datasets that don't strictly adhere to the pre-defined structure, the extraction functions can be molded as per need.

## 📄 License

Sprinkled with love and licensed under the MIT License.

