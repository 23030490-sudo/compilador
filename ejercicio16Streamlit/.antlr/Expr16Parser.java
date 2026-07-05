// Generated from d:/Documents/GitHub/compilador/ejercicio16Streamlit/Expr16.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class Expr16Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, CONSOLE=2, LOG=3, IGUAL=4, PUNTO=5, PUNTO_COMA=6, PARENTESIS_ABRE=7, 
		PARENTESIS_CIERRA=8, IDENTIFICADOR_INVALIDO=9, ID=10, NUMERO=11, COMENTARIO_LINEA=12, 
		WS=13;
	public static final int
		RULE_root = 0, RULE_sentencia = 1, RULE_declaracion = 2, RULE_impresion = 3, 
		RULE_valor = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "sentencia", "declaracion", "impresion", "valor"
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

	@Override
	public String getGrammarFileName() { return "Expr16.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Expr16Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(Expr16Parser.EOF, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LET || _la==CONSOLE) {
				{
				{
				setState(10);
				sentencia();
				}
				}
				setState(15);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(16);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public ImpresionContext impresion() {
			return getRuleContext(ImpresionContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentencia);
		try {
			setState(20);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				declaracion();
				}
				break;
			case CONSOLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(19);
				impresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TerminalNode LET() { return getToken(Expr16Parser.LET, 0); }
		public TerminalNode ID() { return getToken(Expr16Parser.ID, 0); }
		public TerminalNode IGUAL() { return getToken(Expr16Parser.IGUAL, 0); }
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(Expr16Parser.PUNTO_COMA, 0); }
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(LET);
			setState(23);
			match(ID);
			setState(24);
			match(IGUAL);
			setState(25);
			valor();
			setState(26);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImpresionContext extends ParserRuleContext {
		public TerminalNode CONSOLE() { return getToken(Expr16Parser.CONSOLE, 0); }
		public TerminalNode PUNTO() { return getToken(Expr16Parser.PUNTO, 0); }
		public TerminalNode LOG() { return getToken(Expr16Parser.LOG, 0); }
		public TerminalNode PARENTESIS_ABRE() { return getToken(Expr16Parser.PARENTESIS_ABRE, 0); }
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public TerminalNode PARENTESIS_CIERRA() { return getToken(Expr16Parser.PARENTESIS_CIERRA, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(Expr16Parser.PUNTO_COMA, 0); }
		public ImpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impresion; }
	}

	public final ImpresionContext impresion() throws RecognitionException {
		ImpresionContext _localctx = new ImpresionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_impresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(CONSOLE);
			setState(29);
			match(PUNTO);
			setState(30);
			match(LOG);
			setState(31);
			match(PARENTESIS_ABRE);
			setState(32);
			valor();
			setState(33);
			match(PARENTESIS_CIERRA);
			setState(34);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValorContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(Expr16Parser.ID, 0); }
		public TerminalNode NUMERO() { return getToken(Expr16Parser.NUMERO, 0); }
		public TerminalNode IDENTIFICADOR_INVALIDO() { return getToken(Expr16Parser.IDENTIFICADOR_INVALIDO, 0); }
		public ValorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valor; }
	}

	public final ValorContext valor() throws RecognitionException {
		ValorContext _localctx = new ValorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_valor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3584L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\r\'\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0005\u0000\f\b\u0000\n\u0000\f\u0000\u000f\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001\u0015\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0000\u0000\u0005\u0000"+
		"\u0002\u0004\u0006\b\u0000\u0001\u0001\u0000\t\u000b#\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0002\u0014\u0001\u0000\u0000\u0000\u0004\u0016\u0001\u0000"+
		"\u0000\u0000\u0006\u001c\u0001\u0000\u0000\u0000\b$\u0001\u0000\u0000"+
		"\u0000\n\f\u0003\u0002\u0001\u0000\u000b\n\u0001\u0000\u0000\u0000\f\u000f"+
		"\u0001\u0000\u0000\u0000\r\u000b\u0001\u0000\u0000\u0000\r\u000e\u0001"+
		"\u0000\u0000\u0000\u000e\u0010\u0001\u0000\u0000\u0000\u000f\r\u0001\u0000"+
		"\u0000\u0000\u0010\u0011\u0005\u0000\u0000\u0001\u0011\u0001\u0001\u0000"+
		"\u0000\u0000\u0012\u0015\u0003\u0004\u0002\u0000\u0013\u0015\u0003\u0006"+
		"\u0003\u0000\u0014\u0012\u0001\u0000\u0000\u0000\u0014\u0013\u0001\u0000"+
		"\u0000\u0000\u0015\u0003\u0001\u0000\u0000\u0000\u0016\u0017\u0005\u0001"+
		"\u0000\u0000\u0017\u0018\u0005\n\u0000\u0000\u0018\u0019\u0005\u0004\u0000"+
		"\u0000\u0019\u001a\u0003\b\u0004\u0000\u001a\u001b\u0005\u0006\u0000\u0000"+
		"\u001b\u0005\u0001\u0000\u0000\u0000\u001c\u001d\u0005\u0002\u0000\u0000"+
		"\u001d\u001e\u0005\u0005\u0000\u0000\u001e\u001f\u0005\u0003\u0000\u0000"+
		"\u001f \u0005\u0007\u0000\u0000 !\u0003\b\u0004\u0000!\"\u0005\b\u0000"+
		"\u0000\"#\u0005\u0006\u0000\u0000#\u0007\u0001\u0000\u0000\u0000$%\u0007"+
		"\u0000\u0000\u0000%\t\u0001\u0000\u0000\u0000\u0002\r\u0014";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}