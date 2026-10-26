# I/Q Modulation and Wireless Transmission Analysis

<p align="center">
  <b>Hardware-based digital communications experiment</b><br>
  QPSK · 16-QAM · 64-QAM · 256-QAM · Wired vs. Wireless RF
</p>

This project documents a digital communications laboratory experiment investigating how modulation order and wireless propagation conditions affect received signal quality. Signals were generated using a **Rohde & Schwarz SMIQ3B** RF signal generator and examined through constellation and eye diagrams.

> **Main observation:** In the reported wireless measurements, 256-QAM showed noticeable constellation spreading and noise, while QPSK was comparatively robust. Partial antenna obstruction produced distortion and symbol overlap.

## Contents

- [Objectives](#objectives)
- [Equipment and setup](#equipment-and-setup)
- [Modulation schemes](#modulation-schemes)
- [Methodology](#methodology)
- [Results and observations](#results-and-observations)
- [Limitations](#limitations)
- [Repository structure](#repository-structure)

## Objectives

- Investigate coherent in-phase/quadrature (I/Q) modulation.
- Observe QPSK, 16-QAM, 64-QAM, and 256-QAM.
- Compare wired and antenna-based wireless transmission.
- Use constellation and eye diagrams to inspect signal quality.
- Observe the effects of antenna alignment and partial obstruction.

## Equipment and setup

| Item | Details |
|---|---|
| RF signal generator | Rohde & Schwarz SMIQ3B |
| RF frequency | 70 MHz, as stated in the lab report |
| Modulation schemes | QPSK, 16-QAM, 64-QAM, 256-QAM |
| Link conditions | Wired and antenna-based wireless |
| Visual analysis | Constellation diagrams and eye diagrams |

The report also describes QPSK trials at 1 kbit/s and 10 kbit/s. Detailed numerical performance datasets such as BER, EVM, and measured SNR were not reported.

## Modulation schemes

| Scheme | Bits per symbol | Practical trade-off |
|---|---:|---|
| QPSK | 2 | More robust symbol separation |
| 16-QAM | 4 | Higher spectral efficiency, greater sensitivity than QPSK |
| 64-QAM | 6 | Denser constellation and tighter decision margins |
| 256-QAM | 8 | Highest spectral efficiency of the tested schemes; most sensitive to signal impairments |

Higher-order QAM packs more symbols into the constellation. As a result, noise and distortion can make correct symbol decisions more difficult.

## Methodology

1. Configure the SMIQ3B for the selected modulation scheme.
2. Generate and inspect QPSK and QAM signals.
3. Examine constellation and eye diagrams in the wired setup.
4. Repeat observations with antenna-based wireless transmission.
5. Observe signal quality under antenna alignment changes and partial obstruction.
6. Compare the qualitative effects of the channel conditions across modulation orders.

## Results and observations

### QPSK

The report describes QPSK as comparatively robust, with clear symbol separation and minimal overlap. Its antenna-based eye/constellation view provides a useful baseline for comparison.

### 16-QAM

The 16-QAM wired measurements show a denser constellation than QPSK. This illustrates the increased symbol density that accompanies higher bits per symbol.

### 64-QAM and 256-QAM

The wired constellation screenshots show the high symbol density of 64-QAM and 256-QAM. In the wireless observations, higher-order schemes were more affected by imperfect transmission conditions.

### Wireless impairment and obstruction

The report records noticeable noise and spreading in the 256-QAM antenna measurement. A partially blocked antenna condition also produced constellation distortion and symbol overlap.

**Overall finding:** The experiment demonstrated the trade-off between spectral efficiency and robustness. QPSK was comparatively tolerant of the tested conditions, while higher-order QAM—especially 256-QAM—showed more visible degradation.

## Measurement gallery

Add selected, permitted screenshots to `images/` and use the suggested names below. Until those files are added, the image links will not render.

| Suggested image | What it should show |
|---|---|
| `images/qpsk-wireless.png` | QPSK constellation / eye diagram with antenna |
| `images/16qam-wired.png` | 16-QAM wired constellation |
| `images/64qam-wireless.png` | 64-QAM antenna measurement |
| `images/256qam-wireless.png` | 256-QAM antenna measurement |
| `images/antenna-obstructed.png` | Partially blocked antenna condition |

Example Markdown once images are uploaded:

```md
![256-QAM wireless measurement](images/256qam-wireless.png)
```

## Limitations

This repository currently summarizes qualitative observations from the lab report. It does **not** claim quantitative BER, EVM, or SNR results because those values were not established in the supplied report. Screenshots should be described as measured laboratory results, and any future simulated plots or code-generated examples should be clearly labelled as simulations.

## Repository structure

```text
iq-modulation-wireless-analysis/
├── README.md
├── images/
│   └── (add selected lab screenshots here)
├── docs/
│   └── (optional sanitized report or notes)
└── analysis/
    └── (optional scripts or notebooks, if developed)
```

## Skills demonstrated

- Digital communications and I/Q modulation concepts
- QPSK and QAM modulation trade-offs
- RF signal generation using laboratory equipment
- Constellation and eye-diagram interpretation
- Wired versus wireless link comparison
- Qualitative analysis of alignment and obstruction effects
- Technical documentation of experimental results

## Academic context

Based on a Digital Communications laboratory experiment on I/Q coherent modulation and wireless transmission at Hamburg University of Applied Sciences (HAW Hamburg), conducted in July 2025.

Please ensure any report, photograph, or measurement screenshot shared publicly complies with university/course rules and does not expose other participants' personal information.
