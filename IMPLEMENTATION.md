# Categorical Theology Implementation

## Summary

This implementation addresses multiple theological correspondences using category theory:

1. **[pushforward, pull-back] : [Maitreya, Messiah]** - Demonstrates covariant and contravariant functors
2. **[Identity Functor] : [二郎神, Archangel Michael]** - Demonstrates structure preservation across traditions

## Files Added

### 1. categorical_theology.py
A Python module that implements:
- **Pushforward** class: Represents covariant functors (Maitreya)
- **Pullback** class: Represents contravariant functors (Messiah)
- **TheologicalConcept** dataclass: Represents theological concepts with temporal orientation
- **TheologicalFunctor** class: Demonstrates the categorical duality

**Key Features:**
- Generic type system for transformations
- Composition operations for functors
- Detailed explanations of the correspondence
- Concrete examples showing temporal mediation

### 2. pushforward_pullback_experiment.py
A PsychoPy visualization experiment that:
- Displays side-by-side comparison of Pushforward (Maitreya) and Pullback (Messiah)
- Animates directional arrows showing covariant/contravariant nature
- Allows interactive exploration via keyboard controls
- Provides detailed explanations of the categorical duality

**Interactive Controls:**
- SPACE: Toggle between overview and detailed view
- LEFT/RIGHT arrows: Focus on specific concepts
- ESC: Exit

### 3. warrior_deity_experiment.py
A PsychoPy visualization experiment that:
- Displays side-by-side comparison of 二郎神 (Erlang Shen) and Archangel Michael
- Shows the identity functor correspondence between warrior deities
- Allows interactive exploration via keyboard controls
- Provides detailed explanations of the categorical correspondence

**Interactive Controls:**
- SPACE: Toggle between overview and detailed view
- LEFT/RIGHT arrows: Focus on specific deities
- ESC: Exit

### 4. README.md (Updated)
Updated documentation including:
- Overview of categorical theology concepts (Maitreya/Messiah and Erlang Shen/Michael)
- Explanation of pushforward-pullback duality
- Explanation of identity functor correspondence
- Instructions for running both the module and visualizations
- Integration with existing Divine Name Transformation content

## Conceptual Framework

### Pushforward (Covariant) ↔ Maitreya

**Category Theory:**
- Covariant functor that preserves direction of morphisms
- Maps objects and arrows forward through categories

**Theological Analogy:**
- Maitreya: Future Buddha in Buddhist eschatology
- Projects current dharma practice forward to future enlightenment
- Maintains temporal flow: Present → Future

### Pullback (Contravariant) ↔ Messiah

**Category Theory:**
- Contravariant functor that reverses direction of morphisms
- References back to validate forward movement

**Theological Analogy:**
- Messiah: Fulfillment of prophecy in Abrahamic traditions
- References back to ancient covenants and promises
- Reverses temporal reference: Future ← Past

### Identity Functor ↔ 二郎神 (Erlang Shen) and Archangel Michael

**Category Theory:**
- Identity functor preserves categorical structure
- Maps between equivalent structures in different categories
- Maintains essential properties while changing context

**Theological Analogy:**
- Warrior deity archetype appears in different traditions
- 二郎神 (Erlang Shen): Chinese warrior god who defeats demons
- Archangel Michael: Abrahamic warrior angel who defeats Satan
- Both preserve: divine warrior role, protective function, cosmic order maintenance

## Mathematical Rigor

The implementation uses:
- Generic types (TypeVar) for proper functor type safety
- Composition operations that maintain categorical properties
- Clear separation between covariant and contravariant operations

## Usage

```bash
# Run the categorical theology module
python categorical_theology.py

# Run the pushforward-pullback visualization experiment (requires PsychoPy)
python pushforward_pullback_experiment.py

# Run the warrior deity correspondence experiment (requires PsychoPy)
python warrior_deity_experiment.py
```

## Integration

The implementation seamlessly integrates with the existing repository structure:
- Follows the same pattern as `divine_name_experiment.py`
- Uses the same PsychoPy dependency
- Maintains consistent documentation style in README.md
- Complements the existing Id-Ego-Superego framework
- Extends categorical theology with new correspondences

## Security

All code has been verified with CodeQL scanner:
- No security vulnerabilities detected
- Safe type handling throughout
- Proper exception handling in main entry points

## Testing

Manual testing performed:
- ✓ categorical_theology.py runs without errors
- ✓ Output correctly demonstrates pushforward/pullback operations
- ✓ Output correctly demonstrates identity functor correspondence (二郎神 ↔ Archangel Michael)
- ✓ All Python files compile without syntax errors
- ✓ Integration with existing codebase verified
- ✓ No security issues detected

## Changes Summary

### Added Files:
1. `warrior_deity_experiment.py` - New PsychoPy experiment for warrior deity correspondence

### Modified Files:
1. `categorical_theology.py` - Added Erlang Shen and Archangel Michael concepts with identity functor explanation
2. `README.md` - Added documentation for warrior deity correspondence and new experiment
3. `IMPLEMENTATION.md` - Updated with new conceptual framework and usage instructions
