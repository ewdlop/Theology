#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Archangel Michael: Historical and Theological Context

This module addresses the common misconception about the naming relationship
between Archangel Michael and the Renaissance artist Michelangelo Buonarroti.

Historical Clarification:
- Archangel Michael appears in ancient religious texts (Hebrew Bible, New Testament, Quran)
- Michelangelo (the artist, 1475-1564) was named AFTER the archangel, not vice versa
- The artist's full name "Michelangelo" means "Michael the Angel" in Italian
"""

from dataclasses import dataclass
from typing import List
from enum import Enum


class ReligiousText(Enum):
    """Ancient religious texts mentioning Archangel Michael."""
    HEBREW_BIBLE = "Hebrew Bible (Book of Daniel, ~164 BCE)"
    NEW_TESTAMENT = "New Testament (Epistle of Jude, Book of Revelation, ~1st century CE)"
    QURAN = "Quran (Surah 2:98, ~7th century CE)"
    BOOK_OF_ENOCH = "Book of Enoch (~3rd century BCE)"


@dataclass
class HistoricalFigure:
    """Represents a historical figure with temporal context."""
    name: str
    time_period: str
    description: str
    significance: str


class ArchangelMichaelHistory:
    """
    Educational framework for understanding the historical timeline and
    naming relationship between Archangel Michael and Michelangelo Buonarroti.
    """
    
    @staticmethod
    def get_archangel_michael() -> HistoricalFigure:
        """Return information about Archangel Michael."""
        return HistoricalFigure(
            name="Archangel Michael",
            time_period="Ancient texts (3rd century BCE - 1st century CE and earlier)",
            description="Chief of the archangels in Jewish, Christian, and Islamic theology",
            significance="Warrior angel, protector of Israel, defeater of Satan, weigher of souls"
        )
    
    @staticmethod
    def get_michelangelo_artist() -> HistoricalFigure:
        """Return information about Michelangelo Buonarroti."""
        return HistoricalFigure(
            name="Michelangelo di Lodovico Buonarroti Simoni",
            time_period="Renaissance (1475-1564 CE)",
            description="Italian sculptor, painter, architect, and poet",
            significance="Created iconic works including the Sistine Chapel ceiling and 'David' sculpture"
        )
    
    @staticmethod
    def explain_naming_relationship() -> str:
        """Explain the historical naming relationship."""
        return """
        HISTORICAL CLARIFICATION: Archangel Michael vs. Michelangelo
        ================================================================
        
        COMMON MISCONCEPTION:
        ---------------------
        "Was Archangel Michael named after Michelangelo's paintings?"
        
        HISTORICAL REALITY:
        -------------------
        No. The naming relationship is actually the OPPOSITE:
        
        1. ARCHANGEL MICHAEL (Ancient Origin):
           • First mentioned in Hebrew Bible (Book of Daniel, ~164 BCE)
           • Appears in New Testament (1st century CE)
           • Referenced in Quran (7th century CE)
           • Name means "Who is like God?" in Hebrew (Mi-ka-el)
           
        2. MICHELANGELO BUONARROTI (Renaissance Artist):
           • Born: March 6, 1475 CE (over 1,600 years AFTER biblical texts)
           • Full name: Michelangelo di Lodovico Buonarroti Simoni
           • Name "Michelangelo" = "Michael the Angel" in Italian
           • Named AFTER the Archangel Michael, following Christian tradition
        
        TIMELINE:
        ---------
        3rd century BCE: Book of Enoch mentions Michael
        2nd century BCE: Book of Daniel describes Michael as protector
        1st century CE:  New Testament (Jude, Revelation) references Michael
        7th century CE:  Quran mentions Archangel Michael (Mīkāl)
        1475 CE:         Michelangelo Buonarroti born (named after the archangel)
        1508-1512 CE:    Michelangelo paints Sistine Chapel ceiling
        
        SISTINE CHAPEL CONNECTION:
        ---------------------------
        • The Sistine Chapel has an ARCHED (vaulted) ceiling
        • Michelangelo painted it with biblical scenes (1508-1512)
        • The confusion may arise from:
          - "Arc" sounds like "Arch" (architectural feature)
          - "Angle" sounds like "Angel"
          - Both Michelangelo and Archangel Michael share the name "Michael"
        
        CONCLUSION:
        -----------
        Archangel Michael (ancient theological figure) existed in religious 
        texts over 1,600 years before Michelangelo (the artist) was born.
        The artist was named after the archangel, following the Christian 
        tradition of naming children after saints and biblical figures.
        """
    
    @staticmethod
    def get_ancient_references() -> List[str]:
        """List ancient textual references to Archangel Michael."""
        return [
            "Book of Daniel 10:13 - 'Michael, one of the chief princes'",
            "Book of Daniel 12:1 - 'Michael, the great prince who protects your people'",
            "Book of Enoch 20:5 - 'Michael, one of the holy angels'",
            "Epistle of Jude 1:9 - 'Michael the archangel...disputed with the devil'",
            "Book of Revelation 12:7 - 'Michael and his angels fought against the dragon'",
            "Quran 2:98 - 'Michael (Mīkāl) is among the angels'",
            "1 Thessalonians 4:16 - 'The Lord himself shall descend...with the voice of the archangel'"
        ]
    
    @staticmethod
    def michelangelo_works_featuring_angels() -> List[str]:
        """List Michelangelo's artworks featuring angels."""
        return [
            "Sistine Chapel Ceiling (1508-1512) - Various angels in biblical scenes",
            "The Last Judgment (1536-1541) - Angels with trumpets",
            "Manchester Madonna (c. 1497) - Angels in attendance",
            "Doni Tondo (c. 1507) - Angels in background",
            "Tomb of Pope Julius II - Angels as decorative elements"
        ]


def demonstrate_historical_timeline():
    """Display the historical timeline and clarification."""
    print("=" * 80)
    print("ARCHANGEL MICHAEL vs. MICHELANGELO: Historical Timeline")
    print("=" * 80)
    print()
    
    # Get information about both figures
    archangel = ArchangelMichaelHistory.get_archangel_michael()
    artist = ArchangelMichaelHistory.get_michelangelo_artist()
    
    print("ARCHANGEL MICHAEL (Theological Figure):")
    print("-" * 80)
    print(f"Name: {archangel.name}")
    print(f"Time Period: {archangel.time_period}")
    print(f"Description: {archangel.description}")
    print(f"Significance: {archangel.significance}")
    print()
    
    print("MICHELANGELO BUONARROTI (Renaissance Artist):")
    print("-" * 80)
    print(f"Name: {artist.name}")
    print(f"Time Period: {artist.time_period}")
    print(f"Description: {artist.description}")
    print(f"Significance: {artist.significance}")
    print()
    
    # Display the explanation
    print(ArchangelMichaelHistory.explain_naming_relationship())
    
    # Ancient references
    print("\nANCIENT TEXTUAL REFERENCES TO ARCHANGEL MICHAEL:")
    print("-" * 80)
    for ref in ArchangelMichaelHistory.get_ancient_references():
        print(f"  • {ref}")
    print()
    
    # Michelangelo's angel works
    print("MICHELANGELO'S WORKS FEATURING ANGELS:")
    print("-" * 80)
    for work in ArchangelMichaelHistory.michelangelo_works_featuring_angels():
        print(f"  • {work}")
    print()
    
    print("=" * 80)
    print("SUMMARY: Michelangelo (the artist) was named AFTER Archangel Michael,")
    print("         not the other way around. The archangel predates the artist")
    print("         by over 1,600 years!")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_historical_timeline()
