// Generated from d:/Documents/GitHub/compilador/ejercicio16Streamlit/Expr16.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class Expr16Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, CONSOLE=2, LOG=3, IGUAL=4, PUNTO=5, PUNTO_COMA=6, PARENTESIS_ABRE=7, 
		PARENTESIS_CIERRA=8, IDENTIFICADOR_INVALIDO=9, ID=10, NUMERO=11, COMENTARIO_LINEA=12, 
		WS=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LET", "CONSOLE", "LOG", "IGUAL", "PUNTO", "PUNTO_COMA", "PARENTESIS_ABRE", 
			"PARENTESIS_CIERRA", "IDENTIFICADOR_INVALIDO", "ID", "NUMERO", "COMENTARIO_LINEA", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'console'", "'log'", "'='", "'.'", "';'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "CONSOLE", "LOG", "IGUAL", "PUNTO", "PUNTO_COMA", "PARENTESIS_ABRE", 
			"PARENTESIS_CIERRA", "IDENTIFICADOR_INVALIDO", "ID", "NUMERO", "COMENTARIO_LINEA", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public Expr16Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr16.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\rc\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0004\b"+
		"7\b\b\u000b\b\f\b8\u0001\b\u0004\b<\b\b\u000b\b\f\b=\u0001\b\u0005\bA"+
		"\b\b\n\b\f\bD\t\b\u0001\t\u0001\t\u0005\tH\b\t\n\t\f\tK\t\t\u0001\n\u0004"+
		"\nN\b\n\u000b\n\f\nO\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005"+
		"\u000bV\b\u000b\n\u000b\f\u000bY\t\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0004\f^\b\f\u000b\f\f\f_\u0001\f\u0001\f\u0000\u0000\r\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u0001\u0000\u0005\u0001"+
		"\u000009\u0003\u0000AZ__az\u0004\u000009AZ__az\u0002\u0000\n\n\r\r\u0003"+
		"\u0000\t\n\r\r  i\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0001\u001b\u0001\u0000\u0000"+
		"\u0000\u0003\u001f\u0001\u0000\u0000\u0000\u0005\'\u0001\u0000\u0000\u0000"+
		"\u0007+\u0001\u0000\u0000\u0000\t-\u0001\u0000\u0000\u0000\u000b/\u0001"+
		"\u0000\u0000\u0000\r1\u0001\u0000\u0000\u0000\u000f3\u0001\u0000\u0000"+
		"\u0000\u00116\u0001\u0000\u0000\u0000\u0013E\u0001\u0000\u0000\u0000\u0015"+
		"M\u0001\u0000\u0000\u0000\u0017Q\u0001\u0000\u0000\u0000\u0019]\u0001"+
		"\u0000\u0000\u0000\u001b\u001c\u0005l\u0000\u0000\u001c\u001d\u0005e\u0000"+
		"\u0000\u001d\u001e\u0005t\u0000\u0000\u001e\u0002\u0001\u0000\u0000\u0000"+
		"\u001f \u0005c\u0000\u0000 !\u0005o\u0000\u0000!\"\u0005n\u0000\u0000"+
		"\"#\u0005s\u0000\u0000#$\u0005o\u0000\u0000$%\u0005l\u0000\u0000%&\u0005"+
		"e\u0000\u0000&\u0004\u0001\u0000\u0000\u0000\'(\u0005l\u0000\u0000()\u0005"+
		"o\u0000\u0000)*\u0005g\u0000\u0000*\u0006\u0001\u0000\u0000\u0000+,\u0005"+
		"=\u0000\u0000,\b\u0001\u0000\u0000\u0000-.\u0005.\u0000\u0000.\n\u0001"+
		"\u0000\u0000\u0000/0\u0005;\u0000\u00000\f\u0001\u0000\u0000\u000012\u0005"+
		"(\u0000\u00002\u000e\u0001\u0000\u0000\u000034\u0005)\u0000\u00004\u0010"+
		"\u0001\u0000\u0000\u000057\u0007\u0000\u0000\u000065\u0001\u0000\u0000"+
		"\u000078\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u000089\u0001\u0000"+
		"\u0000\u00009;\u0001\u0000\u0000\u0000:<\u0007\u0001\u0000\u0000;:\u0001"+
		"\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000"+
		"=>\u0001\u0000\u0000\u0000>B\u0001\u0000\u0000\u0000?A\u0007\u0002\u0000"+
		"\u0000@?\u0001\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000B@\u0001\u0000"+
		"\u0000\u0000BC\u0001\u0000\u0000\u0000C\u0012\u0001\u0000\u0000\u0000"+
		"DB\u0001\u0000\u0000\u0000EI\u0007\u0001\u0000\u0000FH\u0007\u0002\u0000"+
		"\u0000GF\u0001\u0000\u0000\u0000HK\u0001\u0000\u0000\u0000IG\u0001\u0000"+
		"\u0000\u0000IJ\u0001\u0000\u0000\u0000J\u0014\u0001\u0000\u0000\u0000"+
		"KI\u0001\u0000\u0000\u0000LN\u0007\u0000\u0000\u0000ML\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000"+
		"\u0000\u0000P\u0016\u0001\u0000\u0000\u0000QR\u0005/\u0000\u0000RS\u0005"+
		"/\u0000\u0000SW\u0001\u0000\u0000\u0000TV\b\u0003\u0000\u0000UT\u0001"+
		"\u0000\u0000\u0000VY\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000"+
		"WX\u0001\u0000\u0000\u0000XZ\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000"+
		"\u0000Z[\u0006\u000b\u0000\u0000[\u0018\u0001\u0000\u0000\u0000\\^\u0007"+
		"\u0004\u0000\u0000]\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000"+
		"_]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000"+
		"\u0000ab\u0006\f\u0000\u0000b\u001a\u0001\u0000\u0000\u0000\b\u00008="+
		"BIOW_\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}