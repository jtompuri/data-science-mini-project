"""Tulosmuistioiden (07, 08, 09) yhteiset apufunktiot."""
import numpy as np
import pandas as pd

import config


def vali(arvot):
    """Keskiarvo sekä 10. ja 90. persentiili (sarakkeet mean, p10, p90)."""
    return pd.Series({"mean": arvot.mean(), "p10": arvot.quantile(0.1), "p90": arvot.quantile(0.9)})


def parimatriisi(taulu, arvosarake, puolueet=None):
    """Symmetrinen puolueet × puolueet -taulukko pareittaisista arvoista (sarakkeet a ja b)."""
    puolueet = list(config.MAIN_PARTIES) if puolueet is None else list(puolueet)
    m = taulu.groupby(["a", "b"])[arvosarake].mean().unstack().reindex(index=puolueet, columns=puolueet)
    return (m.fillna(0) + m.T.fillna(0)).rename_axis(index=None, columns=None)


def polarisaatio_kausittain(taulu, sarja="real"):
    """Polarisaation keskiarvo kausittain yhdestä _summary-taulusta."""
    return taulu[taulu["series"] == sarja].groupby("term")["polarisation"].mean()


def samalla_puolella(kausi, a, b):
    """Ovatko puolueet a ja b samalla puolella hallitus–oppositio-rajaa kaudella."""
    hallitus = config.MAIN_GOVERNMENT[kausi]
    return (a in hallitus) == (b in hallitus)


def profiilikoordinaatit(edustajat, sarakkeet):
    """Edustajakartan koordinaatit: profiilien keskitetyt log-suhteet ja kaksi pääkomponenttia."""
    log_p = np.log(edustajat[sarakkeet].to_numpy() + 1e-6)
    log_p = log_p - log_p.mean(axis=1, keepdims=True)
    log_p = log_p - log_p.mean(axis=0)
    _, _, vt = np.linalg.svd(log_p, full_matrices=False)
    return log_p @ vt[:2].T


def klassinen_mds(etaisyysmatriisi):
    """Klassinen moniulotteinen skaalaus kahteen ulottuvuuteen."""
    D2 = np.asarray(etaisyysmatriisi) ** 2
    n = len(D2)
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J @ D2 @ J
    ominaisarvot, ominaisvektorit = np.linalg.eigh(B)
    suurimmat = np.argsort(ominaisarvot)[::-1][:2]
    return ominaisvektorit[:, suurimmat] * np.sqrt(np.clip(ominaisarvot[suurimmat], 0, None))


def kierra_kohti(liikkuva, kohde):
    """Kierto ja peilaus (ei skaalausta), joka vie pistejoukon lähimmäs kohdetta."""
    a = liikkuva - liikkuva.mean(axis=0)
    b = kohde - kohde.mean(axis=0)
    u, _, vt = np.linalg.svd(a.T @ b)
    return a @ (u @ vt)
