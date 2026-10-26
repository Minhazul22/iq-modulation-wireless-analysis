# Experimental notes

These notes summarize the supplied DCL-4 lab report, *I/Q Complex Modulation, wireless*. They intentionally separate qualitative observations from numeric performance metrics.

## Equipment and conditions reported

- Rohde & Schwarz SMIQ3B signal generator.
- RF frequency stated in the report: 70 MHz.
- Modulation schemes: QPSK, 16-QAM, 64-QAM, and 256-QAM.
- Both wired and antenna-based wireless setups were observed.
- The report mentions QPSK trials at 1 kbit/s and 10 kbit/s.

## Qualitative observations

- QPSK was described as robust with clear symbol separation and minimal overlap.
- Higher-order QAM constellations were denser and more sensitive to noise and imperfect transmission conditions.
- The 256-QAM antenna screenshot was described as showing noticeable noise and spreading.
- The partially blocked antenna condition was described as showing distortion and symbol overlap.

## What the report does not quantify

No reproducible numerical dataset for BER, EVM, or received SNR was present in the supplied report. This repository therefore does not assign numeric BER/SNR values or claim a measured threshold at which each modulation scheme fails.

## Evidence locations in the supplied report

- Pages 3–5: QPSK and 16-QAM constellation/eye-diagram observations.
- Page 6: wired 64-QAM and 256-QAM constellation screenshots.
- Pages 7–8: antenna-based QPSK and QAM observations.
- Page 9: partially blocked antenna condition and discussion/conclusion.

Before publishing screenshots or the full report, check course/university sharing rules and remove other participants' personal information where appropriate.
