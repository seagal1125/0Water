# Water Leakage Dispute Documentation Refactoring Plan

## Goal Description
Reorganize the `README.md` file to clearly present the progress of the water leakage dispute and extract the court judgment into a structured data file (`judgments.json`). This will make it easier to track the event's timeline and analyze legal precedents related to waterproofing layers.

## User Review Required
> [!IMPORTANT]
> I will be creating a new file `judgments.json` to store the court judgments. The `README.md` will be significantly rewritten to focus on the event timeline and key takeaways, rather than just a raw chat log.

## Proposed Changes

### Documentation Structure

#### [NEW] [judgments.json](file:///Users/david/Library/Mobile Documents/com~apple~CloudDocs/0漏水/judgments.json)
- Create a JSON file to store court judgments.
- Schema:
  ```json
  [
    {
      "case_id": "112年度訴字第553號",
      "court": "臺灣桃園地方法院",
      "date": "113-07-05",
      "summary": "String summary of the case",
      "waterproofing_points": [
        "Point 1 about waterproofing",
        "Point 2 about waterproofing"
      ],
      "full_text": "Full text of the judgment..."
    }
  ]
  ```

#### [MODIFY] [README.md](file:///Users/david/Library/Mobile Documents/com~apple~CloudDocs/0漏水/README.md)
- **Rename/Retitle**: "漏水爭議事件簿 & 法律實務分析" (Water Leakage Dispute Log & Legal Analysis)
- **Section 1: 事件進度 (Event Progress)**
  - Timeline of Gloria's dispute with the developer.
  - Current status (Negotiation/Pre-legal).
- **Section 2: 核心爭點 (Key Issues)**
  - Local repair vs. Full redo.
  - "素地整平" (Surface leveling) importance.
  - "輕質灌漿牆" (Lightweight grouted wall) risks.
- **Section 3: 法律資源與判決 (Legal Resources & Judgments)**
  - Reference to `judgments.json`.
  - Highlight key takeaways from the Taoyuan District Court judgment.
- **Section 4: 溝通策略 (Communication Strategy)**
  - Templates for "Polite but Firm" messages.
  - Legal basis for withholding payment (5% retention).

## Verification Plan

### Manual Verification
- **Check JSON Validity**: Ensure `judgments.json` is valid JSON.
- **Content Check**: Verify that the extracted judgment contains the correct case number, summary, and waterproofing points.
- **README Readability**: Read the new `README.md` to ensure the timeline is clear and the link to the judgment data is obvious.
