from manim import *

class FullComplianceAnimationEN(Scene):
    def construct(self):
        # ====================== Part 1: Legal & Government Portal Crawler (0-60s) ======================
        self.wait(0.5)
        
        # 0-10s Compliance Check
        title1 = Text("Legal & Government Portal Crawler", font_size=24).to_edge(UP)
        self.play(Write(title1))
        web = Rectangle(width=6, height=4, color=BLUE_C).move_to(ORIGIN)
        robots = Text("robots.txt\nAllowed: /law /policy", font_size=16, color=GREEN).move_to(web)
        self.play(DrawBorderThenFill(web), Write(robots))
        self.wait(2)
        self.play(FadeOut(robots))

        # 10-25s Auto Navigation
        path = VGroup(
            Text("Home", font_size=18),
            Text("Laws & Regulations", font_size=18),
            Text("Digital Trade", font_size=18)
        ).arrange(RIGHT, buff=0.8).move_to(web)
        arrow1 = Arrow(path[0].get_bottom(), path[1].get_bottom(), color=YELLOW)
        arrow2 = Arrow(path[1].get_bottom(), path[2].get_bottom(), color=YELLOW)
        self.play(Write(path), Create(arrow1), Create(arrow2))
        self.wait(2)
        self.play(FadeOut(path, arrow1, arrow2))

        # 25-40s List Parsing & Pagination
        list_ui = VGroup(
            Text("CPTPP 2018.pdf", font_size=16),
            Text("RCEP Clauses.pdf", font_size=16),
            Text("Data Compliance Notice.pdf", font_size=16)
        ).arrange(DOWN, buff=0.3).move_to(web)
        progress = Text("Progress: 3/10", font_size=16, color=GREEN).to_corner(DR)
        self.play(Write(list_ui), Write(progress))
        self.wait(2)
        self.play(FadeOut(list_ui, progress))

        # 40-50s PDF Download
        btn = Rectangle(width=2, height=0.8, color=GREEN).move_to(web)
        btn_text = Text("Download PDF", font_size=16, color=WHITE).move_to(btn)
        bar = Line(LEFT, RIGHT, color=BLUE).scale(0.8).next_to(btn, DOWN, buff=0.3)
        self.play(DrawBorderThenFill(btn), Write(btn_text), Create(bar))
        self.wait(2)
        self.play(FadeOut(btn, btn_text, bar))

        # 50-60s Auto Classification
        folder = VGroup(
            Text("Country-Year-Type", font_size=16),
            Text("Completed", font_size=18, color=GREEN)
        ).arrange(DOWN).move_to(web)
        self.play(Write(folder))
        self.wait(2)
        self.play(FadeOut(web, folder, title1))

        # ====================== Part 2: Semantic Prompt & Keyword Matching (0-45s) ======================
        self.wait(0.5)
        title2 = Text("Semantic Prompt & Keyword Matching", font_size=24).to_edge(UP)
        self.play(Write(title2))

        # 0-10s Keyword Library
        keywords = VGroup(
            Text("Data Residency", font_size=18, color=RED),
            Text("Local Processing", font_size=18, color=ORANGE),
            Text("Adequacy Decision", font_size=18, color=YELLOW)
        ).arrange(RIGHT, buff=0.6).to_edge(UP, buff=1)
        self.play(Write(keywords))
        self.wait(2)

        # 10-30s Scanning & Matching
        doc = Rectangle(width=6, height=3, color=GRAY).move_to(ORIGIN)
        match_text = Text("Match: 98%", font_size=18, color=GREEN).next_to(doc, UP)
        highlight = SurroundingRectangle(match_text, color=YELLOW, buff=0.1)
        self.play(DrawBorderThenFill(doc), Write(match_text), Create(highlight))
        self.wait(2)

        # 30-45s Clause List
        result = VGroup(
            Text("Clause List", font_size=18),
            Text("CPTPP Art.14.1", font_size=16),
            Text("RCEP Ch.12", font_size=16)
        ).arrange(DOWN, buff=0.2).move_to(doc)
        self.play(Transform(doc, result))
        self.wait(2)
        self.play(FadeOut(keywords, match_text, highlight, doc, title2))

        # ====================== Part 3: Intelligent Hierarchical Extraction (0-45s) ======================
        self.wait(0.5)
        title3 = Text("Intelligent Hierarchical Extraction", font_size=24).to_edge(UP)
        self.play(Write(title3))

        # 0-10s OCR Processing
        scan_pdf = Rectangle(width=4, height=2, color=GRAY).move_to(ORIGIN)
        ocr_text = Text("OCR Text Recovery", font_size=18, color=BLUE).move_to(scan_pdf)
        self.play(FadeIn(scan_pdf), Write(ocr_text))
        self.wait(2)
        self.play(FadeOut(scan_pdf, ocr_text))

        # 10-30s Hierarchy Parsing
        tree = VGroup(
            Text("Chapter", font_size=18, color=BLUE),
            Text("├─ Article", font_size=16, color=GREEN),
            Text("└─ Sub-clause", font_size=16, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(Write(tree))
        self.wait(2)

        # 30-45s Structured Output
        table = Rectangle(width=5, height=2, color=GREEN_C)
        table_text = Text("Document | Article | Content", font_size=16).move_to(table)
        end_text = Text("Structured Complete", font_size=20, color=GREEN).next_to(table, DOWN)
        self.play(DrawBorderThenFill(table), Write(table_text), Write(end_text))
        self.wait(3)

        # Final Ending
        self.play(FadeOut(Group(*self.mobjects)))
        final = Text("Compliance Automation Demo Complete", font_size=26, color=BLUE)
        self.play(Write(final))
        self.wait(2)
