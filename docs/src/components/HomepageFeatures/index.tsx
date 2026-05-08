import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

// ── Feature cards ─────────────────────────────────────────────────
type FeatureItem = {
  emoji: string;
  title: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    emoji: '⚡',
    title: 'Real-time results',
    description:
      'Every test row updates live as it runs — pass, fail, skip. No more waiting for the full suite to finish before you know what broke.',
  },
  {
    emoji: '🎯',
    title: 'Select exactly what to run',
    description:
      'Pick individual tests, whole files, or filter by outcome. Parametrized variants are fully expanded and individually selectable.',
  },
  {
    emoji: '⚙️',
    title: 'Works with your existing setup',
    description:
      'pytest-web wraps your existing pytest run. Your conftest.py, fixtures, plugins, and pytest.ini all work exactly as normal.',
  },
  {
    emoji: '🚀',
    title: 'Parallel runs built in',
    description:
      'Set the workers count and pytest-xdist handles the rest. No config changes needed — pytest-web manages the complexity for you.',
  },
  {
    emoji: '📊',
    title: 'One-click Allure reports',
    description:
      'Generate and serve Allure reports with automatic history tracking. Trend graphs and retry counts work out of the box.',
  },
  {
    emoji: '💉',
    title: 'Env var injection',
    description:
      'Pass environment variables to your test run directly from the UI. No need to edit .env files or restart your shell.',
  },
];

function Feature({emoji, title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className={styles.featureEmoji}>{emoji}</div>
      <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
      <p className={styles.featureDesc}>{description}</p>
    </div>
  );
}

// ── Install strip ─────────────────────────────────────────────────
function InstallStrip() {
  return (
    <section className={styles.installStrip}>
      <div className="container">
        <div className={styles.installInner}>
          <span className={styles.installLabel}>Get started in seconds</span>
          <code className={styles.installCode}>pip install pytest-web</code>
          <Link
            className="button button--primary button--md"
            to="/">
            Read the docs →
          </Link>
        </div>
      </div>
    </section>
  );
}

// ── Why section ───────────────────────────────────────────────────
const whyItems = [
  'No config files or setup — just run pytest-web in your project',
  "Zero interference with your test suite — it's a thin wrapper, not a framework",
  'Works with any pytest plugin: Playwright, Django, FastAPI, anyio…',
  'Counters accumulate across runs — history is preserved until you refresh',
  'Cancel a run mid-flight and all xdist workers are cleanly terminated',
  'Fully open source, MIT licensed',
];

function WhySection() {
  return (
    <section className={styles.whySection}>
      <div className="container">
        <div className={styles.whyInner}>
          <div className={styles.whyText}>
            <Heading as="h2">Why pytest-web?</Heading>
            <p className={styles.whySubtitle}>
              The pytest terminal is powerful — but when you're iterating on a
              failing test, hunting through 200 lines of output is slow. pytest-web
              gives you a visual layer on top of the same pytest you already use.
            </p>
            <ul className={styles.whyList}>
              {whyItems.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </div>
          <div className={styles.whyCode}>
            <div className={styles.codeBlock}>
              <div className={styles.codeHeader}>
                <span className={styles.dot} style={{background:'#ff5f57'}}/>
                <span className={styles.dot} style={{background:'#febc2e'}}/>
                <span className={styles.dot} style={{background:'#28c840'}}/>
                <span className={styles.codeTitle}>terminal</span>
              </div>
              <pre className={styles.codePre}>{`$ pip install pytest-web
$ cd your-project
$ pytest-web

                 __            __                     __
    ____  __  __/ /____  _____/ /_     _      _____  / /_
   / __ \/ / / / __/ _ \/ ___/ __/____| | /| / / _ \/ __ \\
  / /_/ / /_/ / /_/  __(__  ) /_/_____/ |/ |/ /  __/ /_/ /
 / .___/\\__, /\\__/\\___/____/\\__/      |__/|__/\\___/_.___/
/_/    /____/

  v0.2.3   http://127.0.0.1:8000   (Ctrl+C to stop)`}
              </pre>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

// ── Export ────────────────────────────────────────────────────────
export default function HomepageFeatures(): ReactNode {
  return (
    <>
      <section className={styles.features}>
        <div className="container">
          <div className="row">
            {FeatureList.map((props, idx) => (
              <Feature key={idx} {...props} />
            ))}
          </div>
        </div>
      </section>
      <InstallStrip />
      <WhySection />
    </>
  );
}
