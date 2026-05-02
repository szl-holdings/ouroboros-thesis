"""Build the v3 paper PDF — Lutar Invariant: An Axiomatic Trust Aggregator."""
from __future__ import annotations

import urllib.request
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
import re
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph as _RLParagraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# -----------------------------------------------------------------------------
# Fonts: download Inter + DM Sans + JetBrains Mono once, register, embed
# -----------------------------------------------------------------------------

FONT_DIR = Path("/tmp/v3-paper-fonts")
FONT_DIR.mkdir(exist_ok=True)

FONTS = {
    "DMSans-Regular": "https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf",
    "DMSans-Bold": "https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf",
    "JetBrainsMono-Regular": "https://github.com/google/fonts/raw/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf",
}

for name, url in FONTS.items():
    p = FONT_DIR / f"{name}.ttf"
    if not p.exists():
        urllib.request.urlretrieve(url, p)
    pdfmetrics.registerFont(TTFont(name, str(p)))

# DM Sans is a single variable font. Register an italic alias for headings if needed.
pdfmetrics.registerFontFamily(
    "DMSans",
    normal="DMSans-Regular",
    bold="DMSans-Bold",
    italic="DMSans-Regular",
    boldItalic="DMSans-Bold",
)

# DM Sans lacks Greek and math glyphs. Register DejaVu Sans (system) as a math
# fallback and provide a helper that wraps known math characters in inline
# <font name="MathFont"> tags so they render correctly in Paragraph flowables.
pdfmetrics.registerFont(TTFont("MathFont", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("MathFont-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

# Characters that DM Sans cannot render. Anything in this set gets wrapped
# in a <font name="MathFont"> span. Order doesn't matter; we do a single pass.
_MATH_CHARS = (
    "\u039b"  # Λ uppercase Lambda
    "\u03bb"  # λ lowercase lambda
    "\u03a3"  # Σ uppercase Sigma
    "\u03c3"  # σ lowercase sigma
    "\u03a0"  # Π uppercase Pi
    "\u03c0"  # π lowercase pi
    "\u2211"  # ∑ summation
    "\u220f"  # ∏ product
    "\u2208"  # ∈ element of
    "\u2209"  # ∉ not element of
    "\u2260"  # ≠ not equal
    "\u2264"  # ≤ less than or equal
    "\u2265"  # ≥ greater than or equal
    "\u2248"  # ≈ approx
    "\u2261"  # ≡ identical
    "\u00b7"  # · middle dot
    "\u2202"  # ∂ partial derivative
    "\u2200"  # ∀ for all
    "\u2203"  # ∃ there exists
    "\u00d7"  # × multiplication
    "\u2192"  # → right arrow
    "\u21d2"  # ⇒ rightwards double arrow
    "\u00b1"  # ± plus or minus
    "\u221a"  # √ square root
    "\u221e"  # ∞ infinity
    "\u2026"  # … ellipsis (DM Sans has it but keep consistent)
    "\u2013"  # – en dash
    "\u2014"  # — em dash
    "\u2032"  # ′ prime
    "\u2713"  # ✓ checkmark
    "\u2717"  # ✗ cross
    "\u2212"  # − Unicode minus sign
    "\u22c5"  # ⋅ dot operator
    "\u2022"  # • bullet
    "\u00a7"  # § section sign
    "\u03b5"  # ε epsilon
)
_MATH_RE = re.compile("([" + re.escape(_MATH_CHARS) + "]+)")


def M(text: str) -> str:
    """Wrap math/greek runs in a <font name='MathFont'> tag so DejaVu renders them.

    Use this on any string passed to Paragraph that may contain Λ, ∑, ∈, ≥, etc.
    Safe to call on plain ASCII (no-op).
    """
    return _MATH_RE.sub(r'<font name="MathFont">\1</font>', text)


def Paragraph(text, style=None, *args, **kwargs):
    """Drop-in replacement for reportlab.platypus.Paragraph that auto-wraps
    Greek/math characters in a DejaVu MathFont span. This keeps DM Sans as
    the body face while ensuring Λ, ∑, ∈, ≥, etc. render correctly.
    """
    if isinstance(text, str):
        text = M(text)
    return _RLParagraph(text, style, *args, **kwargs)

# -----------------------------------------------------------------------------
# Colour palette — restrained, accessible
# -----------------------------------------------------------------------------

INK = HexColor("#1A1A1A")
INK_MUTED = HexColor("#5A5A5A")
INK_FAINT = HexColor("#888888")
ACCENT = HexColor("#01696F")  # Hydra Teal
RULE = HexColor("#D4D1CA")
CODE_BG = HexColor("#F5F4EE")

# -----------------------------------------------------------------------------
# Styles
# -----------------------------------------------------------------------------

styles = getSampleStyleSheet()

title = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    fontName="DMSans-Bold",
    fontSize=22,
    leading=28,
    textColor=INK,
    alignment=0,  # left-align
    spaceAfter=10,
)
subtitle = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontName="DMSans-Regular",
    fontSize=11,
    leading=16,
    textColor=INK_MUTED,
    spaceAfter=4,
)
h1 = ParagraphStyle(
    "H1",
    parent=styles["Heading1"],
    fontName="DMSans-Bold",
    fontSize=15,
    leading=20,
    textColor=INK,
    spaceBefore=18,
    spaceAfter=8,
)
h2 = ParagraphStyle(
    "H2",
    parent=styles["Heading2"],
    fontName="DMSans-Bold",
    fontSize=12,
    leading=16,
    textColor=INK,
    spaceBefore=12,
    spaceAfter=4,
)
body = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="DMSans-Regular",
    fontSize=10.5,
    leading=15,
    textColor=INK,
    spaceAfter=8,
    alignment=4,  # justified
)
body_indent = ParagraphStyle(
    "BodyIndent", parent=body, leftIndent=18, spaceAfter=6,
)
quote = ParagraphStyle(
    "Quote",
    parent=body,
    leftIndent=24,
    rightIndent=12,
    fontName="DMSans-Regular",
    textColor=INK_MUTED,
    fontSize=10,
    leading=14,
    spaceBefore=6,
    spaceAfter=10,
    borderPadding=0,
)
math_block = ParagraphStyle(
    "Math",
    parent=body,
    alignment=1,  # centered
    fontName="DMSans-Regular",
    fontSize=11,
    leading=16,
    spaceBefore=4,
    spaceAfter=10,
    textColor=INK,
)
math_inline_style = body  # inline math uses body style with markup
code = ParagraphStyle(
    "Code",
    parent=styles["Code"],
    fontName="JetBrainsMono-Regular",
    fontSize=8.5,
    leading=11.5,
    textColor=INK,
    backColor=CODE_BG,
    borderPadding=8,
    spaceBefore=4,
    spaceAfter=10,
    leftIndent=8,
    rightIndent=8,
)
caption = ParagraphStyle(
    "Caption",
    parent=body,
    fontSize=8.5,
    leading=11,
    textColor=INK_FAINT,
)
ref_style = ParagraphStyle(
    "Ref",
    parent=body,
    fontSize=9,
    leading=12,
    leftIndent=14,
    firstLineIndent=-14,
    spaceAfter=4,
    alignment=0,
)

# -----------------------------------------------------------------------------
# Math helpers (ReportLab can't render LaTeX; we use HTML markup carefully)
# -----------------------------------------------------------------------------

def m_block(text: str) -> Paragraph:
    """Centered display-style math line. Uses Unicode for the few symbols
    that DM Sans includes (∏, ∑, ∈, ≥, ≤, ⋅, ε), and <super>/<sub> for indices."""
    return Paragraph(text, math_block)


def code_block(text: str) -> Paragraph:
    return Paragraph(text.replace("\n", "<br/>"), code)


# -----------------------------------------------------------------------------
# Document
# -----------------------------------------------------------------------------

OUT = Path("/home/user/workspace/v3-prep/paper/ouroboros-thesis-v3.pdf")

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=LETTER,
    leftMargin=1.0 * inch,
    rightMargin=1.0 * inch,
    topMargin=0.9 * inch,
    bottomMargin=0.9 * inch,
    title="The Lutar Invariant: An Axiomatic Trust Aggregator with Egyptian-Fraction Weight Inspectability",
    author="Perplexity Computer",
)

story: list = []

# Title block
story.append(Paragraph(
    "The Lutar Invariant: An Axiomatic Trust Aggregator "
    "with Egyptian-Fraction Weight Inspectability",
    title,
))
story.append(Paragraph("Stephen Paul Lutar Jr. &nbsp;·&nbsp; SZL Consulting Ltd", subtitle))
story.append(Paragraph(
    'ORCID <a href="https://orcid.org/0009-0001-0110-4173" color="#01696F">'
    '0009-0001-0110-4173</a> &nbsp;·&nbsp; '
    'stephenlutar2@gmail.com &nbsp;·&nbsp; 2 May 2026',
    subtitle,
))
story.append(Paragraph(
    'Version v3 (replaces retracted preprint <a href="https://doi.org/10.5281/zenodo.19951520" '
    'color="#01696F">10.5281/zenodo.19951520</a>) '
    '&nbsp;·&nbsp; Reference: <a href="https://github.com/szl-holdings/ouroboros" color="#01696F">'
    'github.com/szl-holdings/ouroboros</a> @ <font name="JetBrainsMono-Regular" size="9">5f6ee65</font>, '
    'suite 172/172',
    subtitle,
))
story.append(Spacer(1, 14))

# Abstract
story.append(Paragraph("Abstract", h1))
story.append(Paragraph(
    "We define the <b>Lutar Invariant</b> Λ, a scalar trust aggregator over nine independent "
    "runtime axes:",
    body,
))
story.append(m_block("Λ(<b>x</b>; <b>w</b>) = ∏<sub>i=1</sub><super>9</super> x<sub>i</sub><super>w<sub>i</sub></super>, &nbsp;&nbsp; "
                     "x<sub>i</sub> ∈ [0,1], &nbsp; w<sub>i</sub> ≥ 0, &nbsp; ∑ w<sub>i</sub> = 1."))
story.append(Paragraph(
    "Λ is the <b>weighted geometric mean</b> of nine axis scores, with weights drawn from a "
    "transparent Egyptian unit-fraction decomposition. We give four axioms — monotonicity (A1), "
    "zero-pinning (A2), Egyptian inspectability (A3), and page-curve concavity (A4) — and prove "
    "each by explicit numerical witness. The proof suite (22 assertions, all passing) is shipped "
    "in the public reference implementation under an open-source licence and is reproducible via "
    "<font name=\"JetBrainsMono-Regular\" size=\"9.5\">pnpm install &amp;&amp; pnpm exec vitest run "
    "packages/ouroboros/src/lutar-invariant-proof.test.ts</font>.",
    body,
))
story.append(Paragraph(
    "The contribution is the <i>specific combination</i>: weighted-geometric (not arithmetic) "
    "aggregation, distinct unit-fraction weights chosen for inspectability, an explicit four-axiom "
    "set, and a public falsifiable test surface. To the author's knowledge, this combination is "
    "novel; related work on multi-axis trust scoring (cited in §6) uses arithmetic aggregation, "
    "learned weights, or unaxiomatized scalar metrics.",
    body,
))
story.append(Paragraph(
    "This paper does <b>not</b> claim a deployed product, third-party audit, or fielded validation. "
    "The contribution is the formal object Λ, its axiomatization, and the public proof artefact.",
    body,
))

# 1. Motivation
story.append(Paragraph("1. Motivation", h1))
story.append(Paragraph(
    "Bounded-loop AI runtimes accumulate <i>trust signals</i> across heterogeneous concerns: "
    "data freshness, source priority, validator passes, risk-tier escalation, operator approval, "
    "and others. Practitioners increasingly need a single scalar summary of these signals — for "
    "halt conditions, for receipt generation, for audit trails — yet most deployed systems use "
    "either an unaxiomatized weighted sum or a learned black-box score "
    "[Bradatsch et al. 2024; Mahmood et al. 2023].",
    body,
))
story.append(Paragraph(
    "Three properties distinguish a useful trust aggregator from an arbitrary scoring function:",
    body,
))
story.append(Paragraph(
    "<b>1. Monotonicity.</b> Improving any axis must not lower the score.",
    body_indent,
))
story.append(Paragraph(
    "<b>2. Zero-pinning.</b> A single failed axis with positive weight must drive the score to "
    "zero — otherwise the aggregator can mask catastrophic failure of one dimension by averaging "
    "it with healthy ones.",
    body_indent,
))
story.append(Paragraph(
    "<b>3. Inspectability.</b> A practitioner reading a receipt must be able to reproduce the "
    "score by hand, with rational arithmetic, given only the axis scores and the weight set.",
    body_indent,
))
story.append(Paragraph(
    "Weighted arithmetic means satisfy (1) and (3) but fail (2): an arithmetic mean cannot be "
    "driven to zero by any single failing axis unless that axis carries weight 1, which collapses "
    "the aggregator to a univariate quantity. Weighted geometric means satisfy all three, with "
    "the additional concavity property (A4 below) that bounds them above by the corresponding "
    "arithmetic mean (the AM–GM inequality).",
    body,
))

# 2. Definition
story.append(Paragraph("2. Definition", h1))
story.append(Paragraph("2.1 The aggregator", h2))
story.append(Paragraph(
    "Let <b>x</b> = (x<sub>1</sub>, …, x<sub>9</sub>) ∈ [0,1]<super>9</super> be the runtime axis "
    "scores at a given step, and <b>w</b> = (w<sub>1</sub>, …, w<sub>9</sub>) be a non-negative "
    "weight vector with ∑ w<sub>i</sub> = 1. Define",
    body,
))
story.append(m_block(
    "Λ(<b>x</b>; <b>w</b>) = ∏<sub>i=1</sub><super>9</super> x<sub>i</sub><super>w<sub>i</sub></super>"
))
story.append(Paragraph(
    "with the convention that 0<super>0</super> = 1 and the explicit short-circuit: if there exists "
    "i with x<sub>i</sub> = 0 and w<sub>i</sub> &gt; 0, then Λ = 0. The reference implementation "
    "evaluates Λ in log-domain for numerical stability:",
    body,
))
story.append(m_block(
    "Λ = exp( ∑<sub>i: w<sub>i</sub>&gt;0</sub> w<sub>i</sub> · log x<sub>i</sub> )."
))

story.append(Paragraph("2.2 The nine axes", h2))
story.append(Paragraph(
    "The reference implementation labels the axes:",
    body,
))
story.append(m_block(
    "cleanliness, &nbsp; horizon, &nbsp; resonance, &nbsp; frustum, &nbsp; geometry, &nbsp;"
    "invariance, &nbsp; moral, &nbsp; being, &nbsp; non_measurability."
))
story.append(Paragraph(
    "The labels are a runtime-system commitment, not part of the mathematical definition. Any "
    "nine non-negative scalars in [0,1] constitute a valid input to Λ; the labels exist to give "
    "receipts a consistent vocabulary across runs.",
    body,
))

story.append(Paragraph("2.3 Two reference weight sets", h2))
story.append(Paragraph("Two weight sets are exercised by the proof suite:", body))
story.append(Paragraph("<b>Equal weights:</b>", body))
story.append(m_block(
    "<b>w</b><sub>equal</sub> = ( 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9 ), &nbsp;&nbsp; "
    "∑ w<sub>i</sub> = 1."
))
story.append(Paragraph(
    "<b>Egyptian unit-fraction weights</b> (tiered importance: 2 heavy axes, 1 medium, 6 light):",
    body,
))
story.append(m_block(
    "<b>w</b><sub>eg</sub> = ( 1/3, 1/3, 1/9, 1/27, 1/27, 1/27, 1/27, 1/27, 1/27 )."
))
story.append(Paragraph("Verification of ∑ <b>w</b><sub>eg</sub> = 1:", body))
story.append(m_block(
    "1/3 + 1/3 + 1/9 + 6 · (1/27) = 18/27 + 3/27 + 6/27 = 27/27 = 1."
))
story.append(Paragraph(
    "The Egyptian decomposition is the substantive design choice: the weight set is a multiset "
    "of unit fractions (1/n with n a positive integer), so a practitioner can reproduce any "
    "score by hand using rational arithmetic without needing a calculator's floating-point "
    "routine. §3.3 (axiom A3) makes the inspectability property formal.",
    body,
))

# 3. Axioms
story.append(Paragraph("3. Axioms", h1))
story.append(Paragraph(
    "We state four axioms and verify each by numerical witness in the reference implementation. "
    "The witnesses are not surrogates for proofs in the formal-logic sense; they are "
    "<i>falsification tests</i>. A failing assertion would refute the axiom on the test points "
    "exercised, and the axioms are stated such that the implementation either passes them or it "
    "does not.",
    body,
))

# A1
story.append(Paragraph("3.1 A1 — Monotonicity", h2))
story.append(Paragraph(
    "For every i ∈ {1, …, 9} and every <b>x</b> ∈ [0,1]<super>9</super>, if x<sub>i</sub>′ ≥ "
    "x<sub>i</sub> then Λ(<b>x</b>′; <b>w</b>) ≥ Λ(<b>x</b>; <b>w</b>), where <b>x</b>′ agrees "
    "with <b>x</b> outside coordinate i. Strict inequality holds when w<sub>i</sub> &gt; 0 and "
    "the lifted point lies in (0, 1].",
    quote,
))
story.append(Paragraph(
    "<i>Sketch.</i> Differentiate log Λ = ∑ w<sub>j</sub> log x<sub>j</sub> with respect to "
    "x<sub>i</sub>: ∂ log Λ / ∂ x<sub>i</sub> = w<sub>i</sub> / x<sub>i</sub> ≥ 0 on (0,1], "
    "strict when w<sub>i</sub> &gt; 0.",
    body,
))
story.append(Paragraph(
    "<i>Witnesses (4):</i> monotonicity under equal weights; monotonicity under Egyptian weights; "
    "non-increase when any axis is lowered; strict monotonicity when weight is positive. All "
    "four pass.",
    body,
))

# A2
story.append(Paragraph("3.2 A2 — Zero-pinning", h2))
story.append(Paragraph(
    "If there exists i with x<sub>i</sub> = 0 and w<sub>i</sub> &gt; 0, then "
    "Λ(<b>x</b>; <b>w</b>) = 0. Conversely, if x<sub>i</sub> = 0 but w<sub>i</sub> = 0, then "
    "axis i is degenerate and does not affect Λ (since 0<super>0</super> = 1 by convention).",
    quote,
))
story.append(Paragraph(
    "<i>Sketch.</i> The product form makes this immediate: 0<super>w<sub>i</sub></super> = 0 "
    "for any w<sub>i</sub> &gt; 0. The reference implementation uses an explicit short-circuit "
    "so log-domain evaluation never encounters log 0.",
    body,
))
story.append(Paragraph(
    "<i>Witnesses (4):</i> single axis at 0 with equal and Egyptian weights collapses Λ; "
    "multiple zero axes still yield Λ = 0; typical and perfect runs are strictly positive; "
    "zero-weight degenerate axis at 0 does not collapse Λ. All four pass.",
    body,
))

# A3
story.append(Paragraph("3.3 A3 — Egyptian inspectability", h2))
story.append(Paragraph(
    "The standard weight set is a multiset of unit fractions {1/n<sub>k</sub>} with each "
    "n<sub>k</sub> a positive integer, summing exactly to 1 in rational arithmetic. The "
    "aggregator Λ under this weight set is reproducible bit-exactly via two independent "
    "computation paths (direct division and exp-of-log) at IEEE-754 double-precision tolerance.",
    quote,
))
story.append(Paragraph(
    "<i>Sketch.</i> The denominators (3, 3, 9, 27, 27, 27, 27, 27, 27) sum to 1 in rationals "
    "(§2.3). Each 1/n<sub>k</sub> is exactly representable as a double-precision binary fraction "
    "up to rounding; the test verifies rational reconstruction at twelve decimal places.",
    body,
))
story.append(Paragraph(
    "<i>Witnesses (4):</i> sum of unit fractions equals 1 to twelve decimals; bit-exact "
    "reconstruction across two paths; Λ(0.5,…,0.5; <b>w</b><sub>eg</sub>) = 0.5 exactly (the "
    "geometric mean of identical inputs equals that input); the equal-weight set 9 × (1/9) is "
    "also a valid Egyptian decomposition. All four pass.",
    body,
))

# A4
story.append(Paragraph("3.4 A4 — Page-curve concavity", h2))
story.append(Paragraph(
    "Λ is concave on the positive orthant (0,1]<super>9</super>. Equivalently, for any two "
    "points <b>a</b>, <b>b</b> ∈ (0,1]<super>9</super> and any t ∈ [0,1],",
    quote,
))
story.append(m_block(
    "Λ( t·<b>a</b> + (1−t)·<b>b</b>; <b>w</b> ) ≥ t·Λ(<b>a</b>; <b>w</b>) + (1−t)·Λ(<b>b</b>; <b>w</b>)."
))
story.append(Paragraph(
    "As a corollary (the AM–GM inequality applied pointwise),",
    body,
))
story.append(m_block(
    "Λ(<b>x</b>; <b>w</b>) ≤ ∑<sub>i=1</sub><super>9</super> w<sub>i</sub> · x<sub>i</sub>,"
))
story.append(Paragraph(
    "with equality if and only if all x<sub>i</sub> with positive weight are equal.",
    body,
))
story.append(Paragraph(
    "<i>Sketch.</i> The weighted geometric mean is a log-concave function on the positive "
    "orthant; concavity of log Λ plus monotonicity of exp gives concavity of Λ. The "
    "&quot;page curve&quot; name comes from the shape of Λ as one axis is varied with others "
    "fixed — the second-derivative test (numerical second-difference) is the cleanest empirical "
    "handle.",
    body,
))
story.append(Paragraph(
    "<i>Witnesses (4):</i> concavity along a generic line segment in (ε, 1]<super>9</super> "
    "for t ∈ {0.1, 0.25, 0.5, 0.75, 0.9}; concavity on a stress segment with one axis varying "
    "(second-difference ≤ 10<super>−10</super>); AM–GM corollary Λ ≤ ∑ w<sub>i</sub> x<sub>i</sub> "
    "on four representative inputs; equality when all axes are equal. All four pass.",
    body,
))

# 4. Boundary
story.append(Paragraph("4. Boundary and sanity properties", h1))
story.append(Paragraph(
    "A further six assertions exercise the aggregator at semantic boundaries (not new axioms, but "
    "corollaries the implementation must satisfy):",
    body,
))
boundary_items = [
    "Λ(<b>1</b>; <b>w</b>) = 1 for both weight sets (a perfect run).",
    "Λ((0.7, …, 0.7); <b>w</b><sub>equal</sub>) = 0.7 (the geometric mean of identical inputs is that input).",
    "A <i>degraded run</i> with eight axes at 0.9 and one axis at 0.1 yields Λ ≈ 0.707, strictly below the corresponding arithmetic mean ≈ 0.811. This is the headline property: a single weak axis pulls the geometric mean down further than it pulls the arithmetic mean.",
    "Λ is symmetric under axis permutation when weights are uniform.",
    "The axis labels match the runtime declaration verbatim.",
    "Both standard weight sets sum to 1 to twelve decimals.",
]
for k, item in enumerate(boundary_items, 1):
    story.append(Paragraph(f"<b>{k}.</b> &nbsp; {item}", body_indent))
story.append(Paragraph("All six pass.", body))

# 5. Reference implementation
story.append(Paragraph("5. The reference implementation", h1))
story.append(Paragraph("5.1 Overview", h2))
story.append(Paragraph(
    'The runtime <a href="https://github.com/szl-holdings/ouroboros" color="#01696F">'
    'github.com/szl-holdings/ouroboros</a> ships eight modules — loop kernel, depth allocator, '
    'consistency checker, proof-route resolver, risk-tier escalation gate, almanac cycle '
    'advancer, v6 ecosystem-payload schema, and government-readiness manifest — together with '
    'the Λ aggregator and its proof suite. The full test suite contains <b>172 tests across '
    '6 files</b>, all passing on a clean install:',
    body,
))
story.append(code_block(
    "$ pnpm install\n"
    "$ pnpm exec vitest run\n\n"
    " ✓ packages/ouroboros/src/runtime-contract.test.ts     (41 tests)\n"
    " ✓ packages/ouroboros/src/runtime-contract.v4.test.ts  (29 tests)\n"
    " ✓ packages/ouroboros/src/v6-payload.test.ts           (35 tests)\n"
    " ✓ packages/ouroboros/src/lutar-invariant-proof.test.ts (22 tests)\n"
    " ✓ packages/ouroboros/src/gov-readiness.test.ts        (28 tests)\n"
    " ✓ src/runtime-contract.test.ts                        (17 tests)\n\n"
    " Test Files  6 passed (6)\n"
    "      Tests  172 passed (172)"
))
story.append(Paragraph(
    "The 22 Λ tests are the contribution of this paper. The remaining 150 tests exercise the "
    "surrounding runtime contract — those are engineering scaffolding, not part of the central "
    "mathematical claim.",
    body,
))

story.append(Paragraph("5.2 What is and is not unit-tested", h2))
story.append(Paragraph(
    "This paper distinguishes two kinds of test in the suite, and is honest about which back "
    "which claims:",
    body,
))
story.append(Paragraph(
    "<b>Behavioural tests</b> assert that a function or formula returns the correct value on "
    "explicit inputs. The 22 Λ axiom tests are entirely behavioural. So are roughly thirty of "
    "the runtime-contract tests (proof-route resolution, risk-tier escalation, almanac cycle "
    "advance, deep-immutability of contract tables, domain-pack dispatch, operator-approval "
    "gating).",
    body_indent,
))
story.append(Paragraph(
    '<b>Schema regression tests</b> assert that a constant in the source matches the value the '
    'author declared. Tests like <font name="JetBrainsMono-Regular" size="9.5">'
    'expect(SHARED_RUNTIME_SERVICES_V6.length).toBe(16)</font> belong to this category. They are '
    'useful as anti-drift guards but they prove only that the constant has not been edited; they '
    'do not prove that the corresponding runtime services exist as runnable code.',
    body_indent,
))
story.append(Paragraph(
    "The 22 Λ tests are behavioural. No schema regression tests are claimed as proofs.",
    body,
))

story.append(Paragraph("5.3 Reproducing the proof", h2))
story.append(code_block(
    "git clone https://github.com/szl-holdings/ouroboros.git\n"
    "cd ouroboros\n"
    "pnpm install\n"
    "pnpm exec vitest run packages/ouroboros/src/lutar-invariant-proof.test.ts"
))
story.append(Paragraph(
    'Expected output: 22 tests, 22 passed, ~12 ms. A clean snapshot is also stored in '
    '<a href="https://github.com/szl-holdings/ouroboros/blob/main/LUTAR_EVIDENCE.md" color="#01696F">'
    'LUTAR_EVIDENCE.md</a> at the repository root.',
    body,
))

# 6. Related work
story.append(Paragraph("6. Related work", h1))
story.append(Paragraph(
    "<b>Multi-axis trust scoring.</b> Mahmood et al. [2023] survey weighted-sum trust aggregation "
    "in vehicular networks; their formulation is arithmetic and unaxiomatized. Bradatsch et al. "
    "[2024] discuss score-based access control in zero-trust networks, again with arithmetic "
    "combination of factor scores. Gaifulina et al. [2022] propose an &quot;integral user-oriented "
    "trustworthiness metric&quot; by weighted summation. None of these axiomatize the aggregator.",
    body,
))
story.append(Paragraph(
    "<b>Geometric-mean usage in ML evaluation.</b> Henriques et al. [2024] use a 95% confidence "
    "interval of the geometric mean as one of three trust components in machine-learning model "
    "assessment. The geometric mean there is a single statistic over repeated trials, not a "
    "multi-axis aggregator over heterogeneous concerns.",
    body,
))
story.append(Paragraph(
    "<b>Bayesian trust networks.</b> Thomas et al. [2023] build a Bayesian network over trust "
    "factors for medical devices; the propagation rules are conditional probabilities, not a "
    "closed-form aggregator. This is a more expressive but less inspectable construction.",
    body,
))
story.append(Paragraph(
    "<b>Mistrust scoring.</b> Bhaskhar et al. [2023] propose TRUST-LAPSE, a continuous mistrust "
    "score for ML monitoring. The score is learned and is not given a public axiomatization.",
    body,
))
story.append(Paragraph(
    "To the author's knowledge, the combination presented here — <i>weighted-geometric aggregator "
    "with explicit four-axiom statement, Egyptian unit-fraction weight inspectability, and a "
    "public falsifiable test surface</i> — does not appear in the surveyed literature.",
    body,
))

# 7. Limitations
story.append(Paragraph("7. Limitations and what this paper does not establish", h1))
story.append(Paragraph(
    "Stating limitations explicitly is part of the contribution.",
    body,
))
limitations = [
    ("Domain of validity.",
     "The axiom proofs are numerical witnesses on finite test points. They establish that the "
     "IEEE-754 implementation satisfies the axioms on the points exercised; they do not "
     "constitute formal-logic proofs over all of [0,1]<super>9</super>. A future companion in a "
     "proof assistant (Coq, Lean) would close this gap; the closed-form structure of Λ makes such "
     "a proof straightforward but it has not yet been done."),
    ("Axis labels are not proven meaningful.",
     "The nine axis labels (cleanliness, horizon, resonance, frustum, geometry, invariance, "
     "moral, being, non_measurability) are runtime-system commitments. This paper does not claim "
     "they exhaust the relevant trust dimensions of any particular AI system, nor that they are "
     "mutually independent in any deployment. Selecting and operationalising the axes is a "
     "system-design problem outside the scope of the formal object Λ."),
    ("No third-party audit.",
     "The reference implementation has not been audited by any external body. The Empire APEX "
     "engagement on 2026-04-30 (administered by NYSTEC) was procurement <i>counseling</i> for "
     "SZL Consulting Ltd, not technical certification of the runtime."),
    ("No deployed product.",
     "The runtime is an open-source reference. The seven product repositories in the SZL "
     "Holdings organisation — A11oy, Amaru, Sentra, Counsel, Terra, Vessels, Carlota Jo — are "
     "README-stage placeholders at the time of writing (each contains a README, LICENSE, NOTICE, "
     "and SECURITY file, and no source). The author also maintains a separate platform monorepo "
     "(<font name=\"JetBrainsMono-Regular\" size=\"9.5\">szl-holdings/szl-holdings-platform</font>); a fresh-clone audit on 2 May 2026 "
     "confirmed that no <font name=\"JetBrainsMono-Regular\" size=\"9.5\">package.json</font> in that repository declares "
     "<font name=\"JetBrainsMono-Regular\" size=\"9.5\">@szl-holdings/ouroboros</font> as a dependency. The runtime is published as "
     "a standalone reference artefact ready for consumption; it is not currently imported by any "
     "sibling repository, and no fielded validation of Λ is claimed."),
    ("Government-readiness scorecards are self-assessments.",
     'The runtime ships a <font name="JetBrainsMono-Regular" size="9.5">gov-readiness</font> '
     'manifest with platform-readiness scores (A11oy 72/100, Sentra 68/100, Amaru 65/100). These '
     'are founder self-assessments tested for regression, not third-party scores. The '
     'certification path is <font name="JetBrainsMono-Regular" size="9.5">in_progress</font> for '
     'all platforms; none are presently certified.'),
    ("No empirical comparison study.",
     "This paper does not present an empirical comparison of Λ against arithmetic-mean or "
     "learned aggregators on a held-out task. Such a study is straightforward future work and is "
     "not claimed here."),
]
for k, (label, text) in enumerate(limitations, 1):
    story.append(Paragraph(f"<b>{k}. {label}</b> &nbsp; {text}", body))

# 8. Future work
story.append(Paragraph("8. Future work", h1))
future_items = [
    "<b>Formal proof.</b> Mechanise A1–A4 in Lean or Coq.",
    "<b>Empirical comparison.</b> Compare Λ-based halt decisions against arithmetic-mean and "
    "min-aggregator baselines on synthetic 9-axis trust traces.",
    "<b>Weight learning under axiom constraints.</b> Investigate whether <b>w</b> can be learned "
    "from data while preserving Egyptian inspectability (i.e., weights restricted to multisets of "
    "unit fractions).",
    "<b>Implementation of v4 and v6 runtime services.</b> The runtime contract declares a "
    "9-entry validator registry (v4) and a 16-service shared runtime (v6) as routing and "
    "coordination layers; their implementation is the subject of forthcoming work.",
]
for item in future_items:
    story.append(Paragraph(f"• &nbsp; {item}", body_indent))

# 9. Reproducibility
story.append(Paragraph("9. Reproducibility, citation, and licence", h1))
story.append(Paragraph(
    '<b>Reference commit:</b> <a href="https://github.com/szl-holdings/ouroboros/commit/5f6ee65" '
    'color="#01696F"><font name="JetBrainsMono-Regular" size="9.5">5f6ee65</font></a> on '
    '<font name="JetBrainsMono-Regular" size="9.5">main</font> of '
    '<a href="https://github.com/szl-holdings/ouroboros" color="#01696F">'
    'github.com/szl-holdings/ouroboros</a>. The proof file is '
    '<font name="JetBrainsMono-Regular" size="9.5">packages/ouroboros/src/'
    'lutar-invariant-proof.test.ts</font> (278 lines, 22 tests). The evidence summary is '
    '<font name="JetBrainsMono-Regular" size="9.5">LUTAR_EVIDENCE.md</font> at the repository '
    'root.',
    body,
))
story.append(Paragraph("<b>Cite as:</b>", body))
story.append(Paragraph(
    "Lutar, S. P. (2026). <i>The Lutar Invariant: An Axiomatic Trust Aggregator with "
    "Egyptian-Fraction Weight Inspectability.</i> The Ouroboros Thesis, v3. SZL Consulting Ltd. "
    "ORCID 0009-0001-0110-4173.",
    quote,
))
story.append(Paragraph(
    "<b>Licence.</b> Reference implementation is published under the licences declared in the "
    "repository (see <font name=\"JetBrainsMono-Regular\" size=\"9.5\">LICENSE</font> and "
    "<font name=\"JetBrainsMono-Regular\" size=\"9.5\">NOTICE</font>). This paper is released "
    "under CC BY 4.0.",
    body,
))

# References
story.append(Paragraph("References", h1))
refs = [
    ('Bhaskhar, N., Rubin, D. L., &amp; Lee-Messer, C. (2023). TRUST-LAPSE: An Explainable and '
     'Actionable Mistrust Scoring Framework for Model Monitoring. <i>IEEE Transactions on '
     'Artificial Intelligence.</i> <a href="https://doi.org/10.1109/TAI.2023.3272876" '
     'color="#01696F">DOI 10.1109/TAI.2023.3272876</a>.'),
    ('Bradatsch, L., Miroshkin, O., Trkulja, N., &amp; Kargl, F. (2024). Zero Trust Score-based '
     'Network-level Access Control in Enterprise Networks. <i>arXiv preprint.</i> '
     '<a href="https://arxiv.org/abs/2402.08299" color="#01696F">arXiv:2402.08299</a>.'),
    ('Gaifulina, D., Doynikova, E., Novikova, E., &amp; Kotenko, I. (2022). Construction and '
     'Analysis of Integral User-Oriented Trustworthiness Metrics. <i>Electronics, 11(2), 234.</i> '
     '<a href="https://doi.org/10.3390/electronics11020234" color="#01696F">'
     'DOI 10.3390/electronics11020234</a>.'),
    ('Henriques, J., Sousa, J., Gonçalves, L., Paredes, S., Sousa, S., &amp; Rocha, T. (2024). '
     'Machine learning models\' assessment: trust and performance. <i>Medical &amp; Biological '
     'Engineering &amp; Computing.</i> '
     '<a href="https://doi.org/10.1007/s11517-024-03145-5" color="#01696F">'
     'DOI 10.1007/s11517-024-03145-5</a>.'),
    ('Lutar, S. P. (2026a). <i>The Ouroboros Thesis: Looped Computation as a System Primitive '
     'for AI Systems</i> (v1). Zenodo. '
     '<a href="https://doi.org/10.5281/zenodo.19867281" color="#01696F">'
     'DOI 10.5281/zenodo.19867281</a>.'),
    ('Lutar, S. P. (2026b). <i>The Loop Is the Product: An Empirical Companion to the Ouroboros '
     'Thesis</i> (v2). Zenodo. '
     '<a href="https://doi.org/10.5281/zenodo.19934129" color="#01696F">'
     'DOI 10.5281/zenodo.19934129</a>.'),
    ('Mahmood, A., Suzuki, H., Sheng, Q. Z., Siddiqui, S. A., &amp; Ni, W. (2023). Trust in '
     'Vehicles: Toward Context-Aware Trust and Attack Resistance for the Internet of Vehicles. '
     '<i>IEEE Transactions on Intelligent Transportation Systems.</i> '
     '<a href="https://doi.org/10.1109/TITS.2023.3268301" color="#01696F">'
     'DOI 10.1109/TITS.2023.3268301</a>.'),
    ('Thomas, M., Boursalie, O., Samavi, R., &amp; Doyle, T. E. (2023). Data-driven approach to '
     'quantify trust in medical devices using Bayesian networks. <i>Journal of Medical Devices.</i> '
     '<a href="https://doi.org/10.1177/15353702231215893" color="#01696F">'
     'DOI 10.1177/15353702231215893</a>.'),
]
for r in refs:
    story.append(Paragraph(r, ref_style))

# -----------------------------------------------------------------------------
# Header / footer
# -----------------------------------------------------------------------------

def header_footer(c, d):
    c.saveState()
    c.setFont("DMSans-Regular", 8)
    c.setFillColor(INK_FAINT)
    # Header — running title
    c.drawString(d.leftMargin, LETTER[1] - 0.55 * inch,
                 "The Lutar Invariant — Ouroboros Thesis v3 — Lutar, S. P. (2026)")
    # Header rule
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(d.leftMargin, LETTER[1] - 0.62 * inch,
           LETTER[0] - d.rightMargin, LETTER[1] - 0.62 * inch)
    # Footer — page number
    c.drawCentredString(LETTER[0] / 2.0, 0.55 * inch, f"— {d.page} —")
    c.restoreState()

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
