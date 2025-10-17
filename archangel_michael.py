#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Archangel Michael: Theological and Artistic Framework
A framework exploring the theological significance of Archangel Michael
through the lens of artistic representation, particularly Michelangelo's work

This module examines:
- The theological role of Archangel Michael across traditions
- Artistic representations and their theological meanings
- The intersection of divine warrior archetype and artistic expression
"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class MichaelRole(Enum):
    """The various roles of Archangel Michael in theological tradition."""
    DIVINE_WARRIOR = "Divine warrior and protector"
    PSYCHOPOMP = "Guide of souls to the afterlife"
    DRAGON_SLAYER = "Defeater of Satan and evil forces"
    HEAVENLY_PRINCE = "Prince of the heavenly host"
    WEIGHER_OF_SOULS = "Judge who weighs souls at judgment"
    HEALER = "Healing angel in Jewish tradition"


class ArtisticDepiction(Enum):
    """Different artistic representations of Michael across traditions."""
    WARRIOR_WITH_SWORD = "Armed warrior with flaming sword"
    DRAGON_VICTOR = "Standing victorious over dragon/serpent"
    SCALES_OF_JUSTICE = "Holding scales weighing souls"
    ARMORED_GUARDIAN = "Fully armored celestial guardian"
    YOUTHFUL_HERO = "Idealized youthful figure (Renaissance)"


@dataclass
class TheologicalAttribute:
    """Represents a theological attribute of Archangel Michael."""
    name: str
    tradition: str
    description: str
    symbolic_meaning: str
    artistic_representation: ArtisticDepiction


class ArchangelMichael:
    """
    Comprehensive framework for understanding Archangel Michael.
    
    Archangel Michael ("Who is like God?") is one of the most significant
    figures in Jewish, Christian, and Islamic angelology. This class explores
    his multifaceted role through theological and artistic lenses.
    """
    
    @staticmethod
    def get_name_etymology() -> str:
        """
        Explain the etymology and meaning of Michael's name.
        
        Returns:
            Detailed explanation of the name Michael
        """
        return """
        MICHAEL (מִיכָאֵל - Mikha'el)
        ================================
        
        Etymology: Hebrew - "Who is like God?" or "Who is like El?"
        
        Components:
        • Mi (מִי) = "who"
        • Kha (כָ) = "like" or "as"
        • El (אֵל) = "God"
        
        The name itself is a rhetorical question asserting that nothing
        is comparable to God. This name embodies Michael's role as God's
        champion and defender of divine supremacy against prideful rebellion.
        
        The name contrasts with:
        • Lucifer's pride: "I will be like the Most High"
        • Michael's humility: "Who is like God?" (implying: no one)
        """
    
    @staticmethod
    def get_biblical_references() -> List[Tuple[str, str]]:
        """
        Get key biblical references to Archangel Michael.
        
        Returns:
            List of (reference, description) tuples
        """
        return [
            ("Daniel 10:13", "Michael as 'one of the chief princes' helping Daniel"),
            ("Daniel 10:21", "Michael described as 'your prince' (Israel's protector)"),
            ("Daniel 12:1", "Michael as the great prince who protects Daniel's people"),
            ("Jude 1:9", "Michael the archangel disputes with the devil over Moses' body"),
            ("Revelation 12:7-9", "Michael and his angels fight the dragon (Satan)"),
        ]
    
    @staticmethod
    def get_theological_roles() -> List[TheologicalAttribute]:
        """
        Get the various theological roles of Archangel Michael.
        
        Returns:
            List of theological attributes
        """
        return [
            TheologicalAttribute(
                name="Divine Warrior",
                tradition="Christian/Jewish",
                description="Commander of the heavenly armies against evil",
                symbolic_meaning="Divine justice and protection against spiritual warfare",
                artistic_representation=ArtisticDepiction.WARRIOR_WITH_SWORD
            ),
            TheologicalAttribute(
                name="Dragon Slayer",
                tradition="Christian (Revelation)",
                description="Defeats the dragon (Satan) and casts him from heaven",
                symbolic_meaning="Victory of good over evil, light over darkness",
                artistic_representation=ArtisticDepiction.DRAGON_VICTOR
            ),
            TheologicalAttribute(
                name="Psychopomp",
                tradition="Catholic/Orthodox",
                description="Guides and protects souls on their journey to heaven",
                symbolic_meaning="Mediation between earthly and heavenly realms",
                artistic_representation=ArtisticDepiction.SCALES_OF_JUSTICE
            ),
            TheologicalAttribute(
                name="Protector of Israel",
                tradition="Jewish",
                description="Special guardian and advocate for the people of Israel",
                symbolic_meaning="Divine providence and national protection",
                artistic_representation=ArtisticDepiction.ARMORED_GUARDIAN
            ),
        ]
    
    @staticmethod
    def get_michelangelo_connection() -> str:
        """
        Explain the connection between Archangel Michael and Michelangelo.
        
        Returns:
            Detailed explanation of artistic and theological connections
        """
        return """
        ARCHANGEL MICHAEL & MICHELANGELO: ARTISTIC-THEOLOGICAL SYNTHESIS
        ================================================================
        
        The Renaissance master Michelangelo Buonarroti (1475-1564) shared more
        than just a name with the Archangel. His artistic vision embodied many
        of the same qualities attributed to Michael:
        
        NAME CONNECTION:
        ---------------
        • Michelangelo = "Michael Angel" (Michele + Angelo in Italian)
        • The artist's name literally means "Archangel Michael"
        • This nominal connection influenced his artistic identity
        
        SHARED ATTRIBUTES:
        -----------------
        1. Divine Strength
           • Michael: Warrior strength against evil
           • Michelangelo: Sculptural depiction of human physical power
           • Both express divine power made manifest
        
        2. Judgment and Justice
           • Michael: Weighs souls at the Last Judgment
           • Michelangelo: The Last Judgment fresco (Sistine Chapel)
           • Both concerned with divine justice and human accountability
        
        3. Victory Over Darkness
           • Michael: Defeats the dragon/Satan
           • Michelangelo: Light, shadow, and dramatic revelation in art
           • Both illuminate truth against darkness
        
        4. Mediation Between Realms
           • Michael: Bridge between heaven and earth
           • Michelangelo: Art as bridge between divine and human
           • Both function as intermediaries of divine truth
        
        ARTISTIC REPRESENTATIONS:
        ------------------------
        While Michelangelo didn't extensively depict Archangel Michael directly,
        his artistic philosophy embodied Michaelic themes:
        
        • Physical perfection as reflection of divine order
        • Heroic struggle against limitation and sin
        • The terribilità (awesome power) in his figures
        • Divine judgment and human destiny
        
        The Sistine Chapel's Last Judgment (1536-1541) features Christ as judge
        in a pose reminiscent of Michael the weigher of souls, surrounded by
        angels executing divine justice.
        
        THEOLOGICAL IMPLICATION:
        -----------------------
        The artist-archangel connection suggests that human creativity,
        especially in service of depicting divine truth, participates in
        the angelic ministry of revealing and defending divine glory.
        """
    
    @staticmethod
    def get_cross_tradition_comparison() -> str:
        """
        Compare Michael's role across different religious traditions.
        
        Returns:
            Comparative analysis
        """
        return """
        ARCHANGEL MICHAEL ACROSS TRADITIONS
        ===================================
        
        JUDAISM:
        --------
        • High priest of the heavenly sanctuary
        • Advocate for Israel before God
        • Will stand up for Israel at the end of days (Daniel 12:1)
        • Associated with the attribute of Chesed (mercy/loving-kindness)
        
        CHRISTIANITY:
        ------------
        • Leader of God's army against Satan
        • Protector of the Church (replacing protection of Israel)
        • Weigher of souls at individual judgment
        • Patron saint of warriors, police, and paramedics
        • Feast day: September 29 (Michaelmas)
        
        ISLAM:
        ------
        • Mīkāʾīl (ميكائيل) - one of the four archangels
        • Provides nourishment for bodies and souls
        • Controls natural phenomena
        • Less martial than Christian/Jewish traditions
        • Associated with mercy rather than judgment
        
        EASTERN ORTHODOX:
        ----------------
        • Archistrategos (Supreme Commander of Heavenly Hosts)
        • Called "Taxiarch" (commander of the angels)
        • Special veneration with monthly commemoration
        • Protector of the Orthodox Church
        
        COMMON THEMES:
        -------------
        1. Divine authority and power
        2. Protection of the faithful
        3. Opposition to evil forces
        4. Mediation between divine and human realms
        5. Association with judgment or mercy
        """


class MichaelTheology:
    """Advanced theological analysis of Archangel Michael."""
    
    @staticmethod
    def analyze_warrior_archetype() -> str:
        """
        Analyze Michael as the divine warrior archetype.
        
        Returns:
            Analysis of the warrior archetype
        """
        return """
        THE DIVINE WARRIOR ARCHETYPE
        ============================
        
        Archangel Michael embodies the universal archetype of the divine warrior,
        a figure that appears across world mythologies and religions:
        
        ARCHETYPAL ELEMENTS:
        -------------------
        1. Sacred Violence
           • Violence in service of cosmic order
           • Destruction of chaos and evil
           • Not aggression but restoration of peace
        
        2. Cosmic Dualism
           • Clear distinction between good and evil
           • Battle between light and darkness
           • Ultimate victory of divine order
        
        3. Protective Function
           • Guardian of the innocent
           • Defender of the righteous community
           • Shield against spiritual harm
        
        4. Heavenly Authority
           • Commands by divine mandate
           • Acts as God's instrument
           • Executes divine justice
        
        PSYCHOLOGICAL DIMENSION:
        -----------------------
        In Jungian terms, Michael represents:
        
        • The Self: Integrated wholeness defeating ego-driven shadow
        • The Hero: Courageous confrontation with darkness
        • The Logos: Masculine principle of order and discrimination
        
        MODERN RELEVANCE:
        ----------------
        Michael's warrior aspect speaks to:
        
        • Spiritual warfare: Internal struggle against vices
        • Moral courage: Standing for truth despite opposition
        • Protective love: Defending the vulnerable
        • Justice: Confronting systemic evil
        
        The image of Michael defeating the dragon remains potent because
        it symbolizes the eternal human struggle to overcome chaos, both
        internal (psychological) and external (social/spiritual).
        """
    
    @staticmethod
    def explain_theological_significance() -> str:
        """
        Explain the deeper theological significance of Archangel Michael.
        
        Returns:
            Theological explanation
        """
        return """
        THEOLOGICAL SIGNIFICANCE OF ARCHANGEL MICHAEL
        ============================================
        
        1. CHRISTOLOGICAL PARALLEL:
        --------------------------
        Michael's role parallels Christ in several ways:
        
        • Both defeat Satan (Michael in Revelation 12, Christ in broader narrative)
        • Both serve as advocate/intercessor
        • Both associated with final judgment
        • Michael as "type" pointing to Christ the true victor
        
        However, Michael remains creature, not Creator - a crucial distinction
        maintained in orthodox theology.
        
        2. ANGELOLOGY AND HIERARCHY:
        ---------------------------
        Michael's position as archangel reveals:
        
        • Ordered cosmos: Heaven has structure and hierarchy
        • Mediated sovereignty: God rules through appointed agents
        • Creaturely participation: Angels serve God's purposes
        • Community of heaven: The saints are not alone
        
        3. ESCHATOLOGICAL HOPE:
        ----------------------
        Michael's future role (Daniel 12:1, Revelation 12) signifies:
        
        • Final victory is assured
        • Evil will be definitively defeated
        • God's people will be protected through tribulation
        • Cosmic restoration, not mere spiritual redemption
        
        4. LITURGICAL PRESENCE:
        ----------------------
        Invocation of Michael in liturgy:
        
        • Connects earthly worship to heavenly worship
        • Acknowledges angelic participation in liturgy
        • Seeks angelic protection and intercession
        • Maintains awareness of spiritual warfare
        
        5. CULTURAL IMPACT:
        ------------------
        Michael's influence extends beyond strictly religious contexts:
        
        • Military patron: Armies throughout history
        • National symbol: France, Germany, Ukraine, others
        • Artistic inspiration: Countless depictions in art
        • Ethical exemplar: Courage, loyalty, justice
        
        SYNTHESIS:
        ---------
        Archangel Michael represents the convergence of power and service,
        strength and obedience, justice and mercy. His figure demonstrates
        that true authority comes not from self-assertion but from alignment
        with the divine will - a lesson both theological and existential.
        """


def demonstrate_archangel_michael():
    """Demonstrate the Archangel Michael framework with examples."""
    print("=" * 80)
    print("ARCHANGEL MICHAEL: THEOLOGICAL AND ARTISTIC FRAMEWORK")
    print("=" * 80)
    print()
    
    # Name etymology
    print("NAME ETYMOLOGY")
    print("-" * 80)
    print(ArchangelMichael.get_name_etymology())
    print()
    
    # Biblical references
    print("BIBLICAL REFERENCES")
    print("-" * 80)
    references = ArchangelMichael.get_biblical_references()
    for ref, desc in references:
        print(f"• {ref}: {desc}")
    print()
    print()
    
    # Theological roles
    print("THEOLOGICAL ROLES")
    print("-" * 80)
    roles = ArchangelMichael.get_theological_roles()
    for role in roles:
        print(f"{role.name} ({role.tradition})")
        print(f"  Description: {role.description}")
        print(f"  Symbolic Meaning: {role.symbolic_meaning}")
        print(f"  Artistic Form: {role.artistic_representation.value}")
        print()
    print()
    
    # Michelangelo connection
    print("MICHELANGELO CONNECTION")
    print("-" * 80)
    print(ArchangelMichael.get_michelangelo_connection())
    print()
    
    # Cross-tradition comparison
    print("CROSS-TRADITION COMPARISON")
    print("-" * 80)
    print(ArchangelMichael.get_cross_tradition_comparison())
    print()
    
    # Warrior archetype analysis
    print("WARRIOR ARCHETYPE ANALYSIS")
    print("-" * 80)
    print(MichaelTheology.analyze_warrior_archetype())
    print()
    
    # Theological significance
    print("THEOLOGICAL SIGNIFICANCE")
    print("-" * 80)
    print(MichaelTheology.explain_theological_significance())
    print()
    
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_archangel_michael()
